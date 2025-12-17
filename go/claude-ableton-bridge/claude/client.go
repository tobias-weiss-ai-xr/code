package claude

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"time"
)

type Client struct {
	apiKey     string
	httpClient *http.Client
	baseURL    string
}

type Message struct {
	Role    string `json:"role"`
	Content string `json:"content"`
}

type Request struct {
	Model     string    `json:"model"`
	MaxTokens int       `json:"max_tokens"`
	Messages  []Message `json:"messages"`
	System    string    `json:"system,omitempty"`
}

type ContentBlock struct {
	Type string `json:"type"`
	Text string `json:"text"`
}

type Response struct {
	ID      string         `json:"id"`
	Type    string         `json:"type"`
	Role    string         `json:"role"`
	Content []ContentBlock `json:"content"`
	Model   string         `json:"model"`
}

type ErrorResponse struct {
	Type  string `json:"type"`
	Error struct {
		Type    string `json:"type"`
		Message string `json:"message"`
	} `json:"error"`
}

// NewClient creates a new Claude API client with optimized HTTP settings
func NewClient(apiKey string) *Client {
	return &Client{
		apiKey: apiKey,
		httpClient: &http.Client{
			Timeout: 60 * time.Second,
			Transport: &http.Transport{
				MaxIdleConns:        100,
				MaxIdleConnsPerHost: 100,
				IdleConnTimeout:     90 * time.Second,
				DisableKeepAlives:   false,
			},
		},
		baseURL: "https://api.anthropic.com/v1",
	}
}

// GenerateResponse sends a prompt to Claude and returns the response
func (c *Client) GenerateResponse(prompt, context, model string, maxTokens int) (string, error) {
	systemPrompt := c.getSystemPrompt(context)

	reqBody := Request{
		Model:     model,
		MaxTokens: maxTokens,
		Messages: []Message{
			{
				Role:    "user",
				Content: prompt,
			},
		},
		System: systemPrompt,
	}

	jsonData, err := json.Marshal(reqBody)
	if err != nil {
		return "", fmt.Errorf("failed to marshal request: %w", err)
	}

	req, err := http.NewRequest("POST", c.baseURL+"/messages", bytes.NewBuffer(jsonData))
	if err != nil {
		return "", fmt.Errorf("failed to create request: %w", err)
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("x-api-key", c.apiKey)
	req.Header.Set("anthropic-version", "2023-06-01")

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return "", fmt.Errorf("failed to send request: %w", err)
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", fmt.Errorf("failed to read response: %w", err)
	}

	if resp.StatusCode != http.StatusOK {
		var errResp ErrorResponse
		if err := json.Unmarshal(body, &errResp); err != nil {
			return "", fmt.Errorf("API error (status %d): %s", resp.StatusCode, string(body))
		}
		return "", fmt.Errorf("API error: %s", errResp.Error.Message)
	}

	var apiResp Response
	if err := json.Unmarshal(body, &apiResp); err != nil {
		return "", fmt.Errorf("failed to unmarshal response: %w", err)
	}

	if len(apiResp.Content) == 0 {
		return "", fmt.Errorf("empty response from API")
	}

	return apiResp.Content[0].Text, nil
}

// getSystemPrompt returns the appropriate system prompt based on context
func (c *Client) getSystemPrompt(context string) string {
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

// StreamResponse handles streaming responses (simplified version)
func (c *Client) StreamResponse(prompt, context, model string, maxTokens int, callback func(string)) error {
	// Note: Full streaming requires SSE handling
	// This is a simplified version that just calls the regular endpoint
	response, err := c.GenerateResponse(prompt, context, model, maxTokens)
	if err != nil {
		return err
	}

	callback(response)
	return nil
}