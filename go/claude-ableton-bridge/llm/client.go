package llm

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"

	"time"

	"claude-ableton-bridge/config"
)

// LLMClient defines the interface for all Large Language Model clients.
type LLMClient interface {
	GenerateResponse(prompt, context string) (string, error)
}

// Common HTTP client configuration
func newHTTPClient() *http.Client {
	return &http.Client{
		Timeout: 60 * time.Second,
		Transport: &http.Transport{
			MaxIdleConns:        100,
			MaxIdleConnsPerHost: 100,
			IdleConnTimeout:     90 * time.Second,
			DisableKeepAlives:   false,
		},
	}
}

// NewLLMClient is a factory function that creates an LLM client based on configuration.
func NewLLMClient(cfg *config.Config) (LLMClient, error) {
	switch cfg.APIProvider {
	case "claude":
		return NewClaudeClient(cfg.ClaudeAPIKey, cfg.ClaudeModel, cfg.MaxTokens), nil
	case "openai":
		return NewOpenAIClient(cfg.OpenAIAPIKey, cfg.OpenAIBaseURL, cfg.ClaudeModel, cfg.MaxTokens), nil // ClaudeModel used for generic model field
	case "ollama":
		return NewOpenAIClient("", cfg.OpenAIBaseURL, cfg.OllamaModel, cfg.MaxTokens), nil // Ollama does not need API key
	default:
		return nil, fmt.Errorf("unsupported API provider: %s", cfg.APIProvider)
	}
}

// --- Claude Client Implementation ---

type ClaudeClient struct {
	apiKey     string
	model      string
	maxTokens  int
	httpClient *http.Client
	baseURL    string
}

type ClaudeMessage struct {
	Role    string `json:"role"`
	Content string `json:"content"`
}

type ClaudeRequest struct {
	Model     string          `json:"model"`
	MaxTokens int             `json:"max_tokens"`
	Messages  []ClaudeMessage `json:"messages"`
	System    string          `json:"system,omitempty"`
}

type ClaudeContentBlock struct {
	Type string `json:"type"`
	Text string `json:"text"`
}

type ClaudeResponse struct {
	ID      string               `json:"id"`
	Type    string               `json:"type"`
	Role    string               `json:"role"`
	Content []ClaudeContentBlock `json:"content"`
	Model   string               `json:"model"`
}

type ClaudeErrorResponse struct {
	Type  string `json:"type"`
	Error struct {
		Type    string `json:"type"`
		Message string `json:"message"`
	} `json:"error"`
}

func NewClaudeClient(apiKey, model string, maxTokens int) *ClaudeClient {
	return &ClaudeClient{
		apiKey:     apiKey,
		model:      model,
		maxTokens:  maxTokens,
		httpClient: newHTTPClient(),
		baseURL:    "https://api.anthropic.com/v1",
	}
}

func (c *ClaudeClient) GenerateResponse(prompt, context string) (string, error) {
	systemPrompt := getSystemPrompt(context)

	reqBody := ClaudeRequest{
		Model:     c.model,
		MaxTokens: c.maxTokens,
		Messages: []ClaudeMessage{
			{
				Role:    "user",
				Content: prompt,
			},
		},
		System: systemPrompt,
	}

	jsonData, err := json.Marshal(reqBody)
	if err != nil {
		return "", fmt.Errorf("claude: failed to marshal request: %w", err)
	}

	req, err := http.NewRequest("POST", c.baseURL+"/messages", bytes.NewBuffer(jsonData))
	if err != nil {
		return "", fmt.Errorf("claude: failed to create request: %w", err)
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("x-api-key", c.apiKey)
	req.Header.Set("anthropic-version", "2023-06-01")

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return "", fmt.Errorf("claude: failed to send request: %w", err)
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", fmt.Errorf("claude: failed to read response: %w", err)
	}

	if resp.StatusCode != http.StatusOK {
		var errResp ClaudeErrorResponse
		if err := json.Unmarshal(body, &errResp); err != nil {
			return "", fmt.Errorf("claude: API error (status %d): %s", resp.StatusCode, string(body))
		}
		return "", fmt.Errorf("claude: API error: %s", errResp.Error.Message)
	}

	var apiResp ClaudeResponse
	if err := json.Unmarshal(body, &apiResp); err != nil {
		return "", fmt.Errorf("claude: failed to unmarshal response: %w", err)
	}

	if len(apiResp.Content) == 0 {
		return "", fmt.Errorf("claude: empty response from API")
	}

	return apiResp.Content[0].Text, nil
}

// --- OpenAI Compatible Client (for OpenAI and Ollama) ---

type OpenAIClient struct {
	apiKey     string // Empty for Ollama
	model      string
	maxTokens  int
	httpClient *http.Client
	baseURL    string // Can be OpenAI or Ollama base URL
}

type OpenAIMessage struct {
	Role    string `json:"role"`
	Content string `json:"content"`
}

type OpenAIRequest struct {
	Model     string          `json:"model"`
	MaxTokens int             `json:"max_tokens"`
	Messages  []OpenAIMessage `json:"messages"`
}

type OpenAIResponse struct {
	Choices []struct {
		Message OpenAIMessage `json:"message"`
	} `json:"choices"`
}

type OpenAIErrorResponse struct {
	Error struct {
		Message string `json:"message"`
		Type    string `json:"type"`
	} `json:"error"`
}

func NewOpenAIClient(apiKey, baseURL, model string, maxTokens int) *OpenAIClient {
	if baseURL == "" {
		baseURL = "https://api.openai.com/v1" // Default for OpenAI
	}
	return &OpenAIClient{
		apiKey:     apiKey,
		model:      model,
		maxTokens:  maxTokens,
		httpClient: newHTTPClient(),
		baseURL:    baseURL,
	}
}

func (o *OpenAIClient) GenerateResponse(prompt, context string) (string, error) {
	systemPrompt := getSystemPrompt(context)

	messages := []OpenAIMessage{
		{Role: "system", Content: systemPrompt},
		{Role: "user", Content: prompt},
	}

	reqBody := OpenAIRequest{
		Model:     o.model,
		MaxTokens: o.maxTokens,
		Messages:  messages,
	}

	jsonData, err := json.Marshal(reqBody)
	if err != nil {
		return "", fmt.Errorf("openai-compat: failed to marshal request: %w", err)
	}

	req, err := http.NewRequest("POST", o.baseURL+"/chat/completions", bytes.NewBuffer(jsonData))
	if err != nil {
		return "", fmt.Errorf("openai-compat: failed to create request: %w", err)
	}

	req.Header.Set("Content-Type", "application/json")
	if o.apiKey != "" {
		req.Header.Set("Authorization", "Bearer "+o.apiKey)
	}

	resp, err := o.httpClient.Do(req)
	if err != nil {
		return "", fmt.Errorf("openai-compat: failed to send request: %w", err)
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", fmt.Errorf("openai-compat: failed to read response: %w", err)
	}

	if resp.StatusCode != http.StatusOK {
		var errResp OpenAIErrorResponse
		if err := json.Unmarshal(body, &errResp); err != nil {
			return "", fmt.Errorf("openai-compat: API error (status %d): %s", resp.StatusCode, string(body))
		}
		return "", fmt.Errorf("openai-compat: API error: %s", errResp.Error.Message)
	}

	var apiResp OpenAIResponse
	if err := json.Unmarshal(body, &apiResp); err != nil {
		return "", fmt.Errorf("openai-compat: failed to unmarshal response: %w", err)
	}

	if len(apiResp.Choices) == 0 || apiResp.Choices[0].Message.Content == "" {
		return "", fmt.Errorf("openai-compat: empty response from API")
	}

	return apiResp.Choices[0].Message.Content, nil
}

// getSystemPrompt returns the appropriate system prompt based on context
func getSystemPrompt(context string) string {
	systemPrompts := map[string]string{
		"music": `You are a music production assistant for Ableton Live. Generate musical ideas in valid JSON format. 
Always structure your responses clearly and include valid JSON that can be parsed.`,

		"midi": `You are a MIDI data generator for Ableton Live. Return ONLY valid JSON with precise MIDI data.
Format your response as: {"notes": [{"note": 60, "velocity": 80, "duration": 500, "time": 0}]}
- note: MIDI note number (0-127)
- velocity: Note velocity (0-127)
- duration: Note duration in milliseconds
- time: Time offset from start in milliseconds
Always ensure the JSON is valid and parseable.`,

		"chord": `You are a chord progression generator. Return JSON with chord information.
Format: {"chords": [{"name": "Cmaj7", "notes": [60, 64, 67, 71], "duration": 1000}]}`,

		"effects": `You are an audio effects specialist for Ableton Live. Suggest parameter values in JSON format.
Format: {"effect": "reverb", "parameters": {"mix": 0.3, "decay": 2.5, "predelay": 20}}
All parameter values should be normalized (0.0 to 1.0) unless specified otherwise.`,

		"drums": `You are a drum pattern generator. Return JSON with drum MIDI data using standard GM drum mapping.
Format: {"pattern": [{"note": 36, "velocity": 100, "time": 0}]}
Common drums: 36=kick, 38=snare, 42=closed_hat, 46=open_hat, 49=crash`,

		"melody": `You are a melody generator. Create melodic sequences in JSON format.
Format: {"melody": {"key": "C", "scale": "major", "notes": [{"note": 60, "velocity": 80, "duration": 500, "time": 0}]}}`,

		"default": `You are a helpful music production assistant for Ableton Live. Provide clear, actionable advice.
When generating musical data, always use valid JSON format.`,
	}

	if prompt, ok := systemPrompts[context]; ok {
		return prompt
	}
	return systemPrompts["default"]
}