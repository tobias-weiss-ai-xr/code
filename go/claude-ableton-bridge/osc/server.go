package osc

import (
	"fmt"
	"log"
	"sync"
	"time"

	"claude-ableton-bridge/cache"
	"claude-ableton-bridge/claude"
	"claude-ableton-bridge/config"
	"claude-ableton-bridge/midi"

	"github.com/hypebeast/go-osc/osc"
)

type Server struct {
	config       *config.Config
	claudeClient *claude.Client
	oscServer    *osc.Server
	oscClient    *osc.Client
	cache        *cache.Cache
	wg           sync.WaitGroup
	stopChan     chan bool
}

func NewServer(cfg *config.Config, claudeClient *claude.Client) (*Server, error) {
	addr := fmt.Sprintf("%s:%d", cfg.OSCHost, cfg.OSCReceivePort)

	oscServer := &osc.Server{
		Addr:       addr,
		Dispatcher: osc.NewStandardDispatcher(),
	}

	oscClient := osc.NewClient(cfg.OSCHost, cfg.OSCSendPort)

	var cacheInstance *cache.Cache
	if cfg.EnableCache {
		cacheInstance = cache.NewCache(time.Duration(cfg.CacheTTL) * time.Second)
	}

	return &Server{
		config:       cfg,
		claudeClient: claudeClient,
		oscServer:    oscServer,
		oscClient:    oscClient,
		cache:        cacheInstance,
		stopChan:     make(chan bool),
	}, nil
}

func (s *Server) Start() error {
	// Register OSC message handlers
	s.AddMsgHandler("/claude/prompt", s.handlePrompt)
	s.AddMsgHandler("/claude/midi", s.handleMIDIRequest)
	s.AddMsgHandler("/claude/chord", s.handleChordRequest)
	s.AddMsgHandler("/claude/drums", s.handleDrumsRequest)
	s.AddMsgHandler("/claude/melody", s.handleMelodyRequest)
	s.AddMsgHandler("/claude/effects", s.handleEffectsRequest)
	s.AddMsgHandler("/claude/context", s.handleContextRequest)
	s.AddMsgHandler("/claude/ping", s.handlePing)

	log.Printf("OSC Server listening on %s", s.oscServer.Addr)

	return s.oscServer.ListenAndServe()
}

func (s *Server) Stop() {
	s.oscServer.CloseConnection() // Use CloseConnection instead of closing stopChan
	s.wg.Wait()
}

// AddMsgHandler is a helper to register message handlers with the StandardDispatcher
func (s *Server) AddMsgHandler(addr string, handler osc.HandlerFunc) error {
	if dispatcher, ok := s.oscServer.Dispatcher.(*osc.StandardDispatcher); ok {
		return dispatcher.AddMsgHandler(addr, handler)
	}
	return fmt.Errorf("dispatcher is not a StandardDispatcher or not initialized")
}

func (s *Server) dispatchMessage(msg *osc.Message) {
	// This function is no longer needed as the StandardDispatcher handles dispatching.
	// It's kept here as a placeholder for potential future custom dispatching.
	log.Printf("Received message %s but not dispatched by custom logic. Should be handled by StandardDispatcher.", msg.Address)
}

func (s *Server) handlePrompt(msg *osc.Message) {
	if len(msg.Arguments) == 0 {
		s.sendError("No prompt provided")
		return
	}

	prompt, ok := msg.Arguments[0].(string)
	if !ok {
		s.sendError("Invalid prompt format")
		return
	}

	context := "music"
	if len(msg.Arguments) > 1 {
		if ctx, ok := msg.Arguments[1].(string); ok {
			context = ctx
		}
	}

	log.Printf("Received prompt: %s (context: %s)", prompt, context)

	s.wg.Add(1)
	go func() {
		defer s.wg.Done()
		s.processPrompt(prompt, context)
	}()
}

func (s *Server) processPrompt(prompt, context string) {
	// Check cache if enabled
	if s.cache != nil {
		cacheKey := s.cache.Hash(prompt, context)
		if cached, found := s.cache.Get(cacheKey); found {
			log.Printf("Cache hit for prompt")
			s.sendResponse(cached)
			return
		}
	}

	response, err := s.claudeClient.GenerateResponse(
		prompt,
		context,
		s.config.ClaudeModel,
		s.config.MaxTokens,
	)

	if err != nil {
		s.sendError(fmt.Sprintf("Claude API error: %v", err))
		return
	}

	// Store in cache if enabled
	if s.cache != nil {
		cacheKey := s.cache.Hash(prompt, context)
		s.cache.Set(cacheKey, response)
	}

	log.Printf("Sending response to Max (length: %d bytes)", len(response))
	s.sendResponse(response)
}

func (s *Server) handleMIDIRequest(msg *osc.Message) {
	s.handleMusicalRequest(msg, "midi", "/claude/midi/data")
}

func (s *Server) handleChordRequest(msg *osc.Message) {
	s.handleMusicalRequest(msg, "chord", "/claude/chord/data")
}

func (s *Server) handleDrumsRequest(msg *osc.Message) {
	s.handleMusicalRequest(msg, "drums", "/claude/drums/data")
}

func (s *Server) handleMelodyRequest(msg *osc.Message) {
	s.handleMusicalRequest(msg, "melody", "/claude/melody/data")
}

func (s *Server) handleMusicalRequest(msg *osc.Message, context, responsePath string) {
	if len(msg.Arguments) == 0 {
		s.sendError(fmt.Sprintf("No %s prompt provided", context))
		return
	}

	prompt, ok := msg.Arguments[0].(string)
	if !ok {
		s.sendError(fmt.Sprintf("Invalid %s prompt format", context))
		return
	}

	log.Printf("Received %s request: %s", context, prompt)

	s.wg.Add(1)
	go func() {
		defer s.wg.Done()

		// Check cache
		if s.cache != nil {
			cacheKey := s.cache.Hash(prompt, context)
			if cached, found := s.cache.Get(cacheKey); found {
				log.Printf("Cache hit for %s request", context)
				midiData, err := midi.ParseClaudeResponse(cached)
				if err == nil {
					s.sendMIDIData(midiData, responsePath)
					return
				}
			}
		}

		response, err := s.claudeClient.GenerateResponse(
			prompt,
			context,
			s.config.ClaudeModel,
			s.config.MaxTokens,
		)

		if err != nil {
			s.sendError(fmt.Sprintf("Claude API error: %v", err))
			return
		}

		// Store in cache
		if s.cache != nil {
			cacheKey := s.cache.Hash(prompt, context)
			s.cache.Set(cacheKey, response)
		}

		// Parse MIDI data
		midiData, err := midi.ParseClaudeResponse(response)
		if err != nil {
			s.sendError(fmt.Sprintf("MIDI parsing error: %v", err))
			s.sendResponse(response) // Send raw response as fallback
			return
		}

		s.sendMIDIData(midiData, responsePath)
	}()
}

func (s *Server) handleEffectsRequest(msg *osc.Message) {
	if len(msg.Arguments) == 0 {
		s.sendError("No effects prompt provided")
		return
	}

	prompt, ok := msg.Arguments[0].(string)
	if !ok {
		s.sendError("Invalid effects prompt format")
		return
	}

	log.Printf("Received effects request: %s", prompt)

	s.wg.Add(1)
	go func() {
		defer s.wg.Done()
		s.processPrompt(prompt, "effects")
	}()
}

func (s *Server) handleContextRequest(msg *osc.Message) {
	log.Printf("Received context request")
	s.sendResponse("Context request acknowledged - feature not yet implemented")
}

func (s *Server) handlePing(msg *osc.Message) {
	log.Printf("Received ping")
	pongMsg := osc.NewMessage("/claude/pong")
	pongMsg.Append("alive")
	s.oscClient.Send(pongMsg)
}

func (s *Server) sendResponse(response string) {
	msg := osc.NewMessage("/claude/response")
	msg.Append(response)

	if err := s.oscClient.Send(msg); err != nil {
		log.Printf("Failed to send response: %v", err)
	}
}

func (s *Server) sendError(errMsg string) {
	log.Printf("Error: %s", errMsg)

	msg := osc.NewMessage("/claude/error")
	msg.Append(errMsg)

	if err := s.oscClient.Send(msg); err != nil {
		log.Printf("Failed to send error: %v", err)
	}
}

func (s *Server) sendMIDIData(midiData *midi.Data, path string) {
	jsonData, err := midiData.ToJSON()
	if err != nil {
		s.sendError(fmt.Sprintf("Failed to serialize MIDI data: %v", err))
		return
	}

	msg := osc.NewMessage(path)
	msg.Append(string(jsonData))

	if err := s.oscClient.Send(msg); err != nil {
		log.Printf("Failed to send MIDI data: %v", err)
	}
}