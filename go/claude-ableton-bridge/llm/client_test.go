package llm

import (
	"claude-ableton-bridge/config"
	"fmt"
	"encoding/json"
	"io"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"

)

// Mock HTTP server for Claude API
func mockClaudeServer(t *testing.T, statusCode int, responseBody string, expectedAPIKey, expectedModel string) *httptest.Server {
	return httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path != "/messages" {
			t.Errorf("Unexpected Claude API path: %s", r.URL.Path)
		}
		if r.Header.Get("x-api-key") != expectedAPIKey {
			t.Errorf("Missing or incorrect Claude API key: %s", r.Header.Get("x-api-key"))
		}
		if r.Header.Get("anthropic-version") != "2023-06-01" {
			t.Errorf("Missing or incorrect Anthropic-Version header: %s", r.Header.Get("anthropic-version"))
		}
		if r.Method != "POST" {
			t.Errorf("Expected POST method, got %s", r.Method)
		}

		bodyBytes, err := io.ReadAll(r.Body)
		if err != nil {
			t.Fatalf("Failed to read request body: %v", err)
		}
		var req ClaudeRequest
		if err := json.Unmarshal(bodyBytes, &req); err != nil {
			t.Fatalf("Failed to unmarshal Claude request: %v", err)
		}
		if req.Model != expectedModel {
			t.Errorf("Expected Claude model %s, got %s", expectedModel, req.Model)
		}

		w.WriteHeader(statusCode)
		fmt.Fprintln(w, responseBody)
	}))
}

// Mock HTTP server for OpenAI-compatible API
func mockOpenAIServer(t *testing.T, statusCode int, responseBody string, expectedAPIKey, expectedModel string) *httptest.Server {
	return httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path != "/chat/completions" {
			t.Errorf("Unexpected OpenAI API path: %s", r.URL.Path)
		}
		if expectedAPIKey != "" && r.Header.Get("Authorization") != "Bearer "+expectedAPIKey {
			t.Errorf("Missing or incorrect OpenAI API key: %s", r.Header.Get("Authorization"))
		}
		if r.Method != "POST" {
			t.Errorf("Expected POST method, got %s", r.Method)
		}

		bodyBytes, err := io.ReadAll(r.Body)
		if err != nil {
			t.Fatalf("Failed to read request body: %v", err)
		}
		var req OpenAIRequest
		if err := json.Unmarshal(bodyBytes, &req); err != nil {
			t.Fatalf("Failed to unmarshal OpenAI request: %v", err)
		}
		if req.Model != expectedModel {
			t.Errorf("Expected OpenAI model %s, got %s", expectedModel, req.Model)
		}

		w.WriteHeader(statusCode)
		fmt.Fprintln(w, responseBody)
	}))
}

func TestNewLLMClient(t *testing.T) {
	t.Run("Claude client creation", func(t *testing.T) {
		cfg := &config.Config{APIProvider: "claude", ClaudeAPIKey: "test-claude", ClaudeModel: "opus", MaxTokens: 100}
		client, err := NewLLMClient(cfg)
		if err != nil {
			t.Fatalf("NewLLMClient failed for Claude: %v", err)
		}
		if _, ok := client.(*ClaudeClient); !ok {
			t.Errorf("Expected ClaudeClient, got %T", client)
		}
	})

	t.Run("OpenAI client creation", func(t *testing.T) {
		cfg := &config.Config{APIProvider: "openai", OpenAIAPIKey: "test-openai", ClaudeModel: "gpt-4", MaxTokens: 100} // ClaudeModel maps to generic model
		client, err := NewLLMClient(cfg)
		if err != nil {
			t.Fatalf("NewLLMClient failed for OpenAI: %v", err)
		}
		if _, ok := client.(*OpenAIClient); !ok {
			t.Errorf("Expected OpenAIClient, got %T", client)
		}
	})

	t.Run("Ollama client creation", func(t *testing.T) {
		cfg := &config.Config{APIProvider: "ollama", OpenAIBaseURL: "http://localhost:11434/v1", OllamaModel: "llama2", MaxTokens: 100}
		client, err := NewLLMClient(cfg)
		if err != nil {
			t.Fatalf("NewLLMClient failed for Ollama: %v", err)
		}
		if _, ok := client.(*OpenAIClient); !ok {
			t.Errorf("Expected OpenAIClient (for Ollama), got %T", client)
		}
		// Verify no API key for Ollama
		if oc, ok := client.(*OpenAIClient); ok && oc.apiKey != "" {
			t.Errorf("Ollama client should not have an API key, got %s", oc.apiKey)
		}
		if oc, ok := client.(*OpenAIClient); ok && oc.baseURL != "http://localhost:11434/v1" {
			t.Errorf("Ollama client base URL mismatch, got %s", oc.baseURL)
		}
	})

	t.Run("Unsupported provider", func(t *testing.T) {
		cfg := &config.Config{APIProvider: "unsupported"}
		_, err := NewLLMClient(cfg)
		if err == nil {
			t.Error("Expected error for unsupported provider, got nil")
		}
	})
}

func TestClaudeClient_GenerateResponse(t *testing.T) {
	apiKey := "test-claude-key"
	model := "claude-test-model"
	expectedResponse := `{"content":[{"type":"text","text":"Hello from Claude"}]}`

	t.Run("Success", func(t *testing.T) {
		server := mockClaudeServer(t, http.StatusOK, expectedResponse, apiKey, model)
		defer server.Close()

		client := NewClaudeClient(apiKey, model, 200)
		client.baseURL = server.URL // Override with mock server URL

		response, err := client.GenerateResponse("test prompt", "default")
		if err != nil {
			t.Fatalf("GenerateResponse failed: %v", err)
		}
		if response != "Hello from Claude" {
			t.Errorf("Expected 'Hello from Claude', got '%s'", response)
		}
	})

	t.Run("API Error", func(t *testing.T) {
		errorResponse := `{"type":"error","error":{"type":"server_error","message":"Internal Server Error"}}`
		server := mockClaudeServer(t, http.StatusInternalServerError, errorResponse, apiKey, model)
		defer server.Close()

		client := NewClaudeClient(apiKey, model, 200)
		client.baseURL = server.URL

		_, err := client.GenerateResponse("test prompt", "default")
		if err == nil || !strings.Contains(err.Error(), "API error: Internal Server Error") {
			t.Errorf("Expected API error, got: %v", err)
		}
	})

	t.Run("Empty Response", func(t *testing.T) {
		emptyResponse := `{"content":[]}`
		server := mockClaudeServer(t, http.StatusOK, emptyResponse, apiKey, model)
		defer server.Close()

		client := NewClaudeClient(apiKey, model, 200)
		client.baseURL = server.URL

		_, err := client.GenerateResponse("test prompt", "default")
		if err == nil || !strings.Contains(err.Error(), "empty response from API") {
			t.Errorf("Expected empty response error, got: %v", err)
		}
	})

	t.Run("Malformed JSON Response", func(t *testing.T) {
		malformedResponse := `{"content":`
		server := mockClaudeServer(t, http.StatusOK, malformedResponse, apiKey, model)
		defer server.Close()

		client := NewClaudeClient(apiKey, model, 200)
		client.baseURL = server.URL

		_, err := client.GenerateResponse("test prompt", "default")
		if err == nil || !strings.Contains(err.Error(), "failed to unmarshal response") {
			t.Errorf("Expected unmarshal error, got: %v", err)
		}
	})
}

func TestOpenAIClient_GenerateResponse(t *testing.T) {
	apiKey := "test-openai-key"
	model := "gpt-test-model"
	expectedResponse := `{"choices":[{"message":{"role":"assistant","content":"Hello from OpenAI"}}], "id": "chatcmpl-123", "object": "chat.completion", "created": 123}`

	t.Run("Success - OpenAI", func(t *testing.T) {
		server := mockOpenAIServer(t, http.StatusOK, expectedResponse, apiKey, model)
		defer server.Close()

		client := NewOpenAIClient(apiKey, server.URL, model, 200) // Override with mock server URL

		response, err := client.GenerateResponse("test prompt", "default")
		if err != nil {
			t.Fatalf("GenerateResponse failed: %v", err)
		}
		if response != "Hello from OpenAI" {
			t.Errorf("Expected 'Hello from OpenAI', got '%s'", response)
		}
	})

	t.Run("Success - Ollama (no API key)", func(t *testing.T) {
		server := mockOpenAIServer(t, http.StatusOK, expectedResponse, "", "llama2-test") // Ollama no API key
		defer server.Close()

		client := NewOpenAIClient("", server.URL, "llama2-test", 200) // Override with mock server URL, no API key
		response, err := client.GenerateResponse("test prompt", "default")
		if err != nil {
			t.Fatalf("GenerateResponse failed: %v", err)
		}
		if response != "Hello from OpenAI" {
			t.Errorf("Expected 'Hello from OpenAI', got '%s'", response)
		}
	})

	t.Run("API Error", func(t *testing.T) {
		errorResponse := `{"error":{"message":"Internal Server Error","type":"server_error"}}`
		server := mockOpenAIServer(t, http.StatusInternalServerError, errorResponse, apiKey, model)
		defer server.Close()

		client := NewOpenAIClient(apiKey, server.URL, model, 200)

		_, err := client.GenerateResponse("test prompt", "default")
		if err == nil || !strings.Contains(err.Error(), "API error: Internal Server Error") {
			t.Errorf("Expected API error, got: %v", err)
		}
	})

	t.Run("Empty Response", func(t *testing.T) {
		emptyResponse := `{"choices":[]}`
		server := mockOpenAIServer(t, http.StatusOK, emptyResponse, apiKey, model)
		defer server.Close()

		client := NewOpenAIClient(apiKey, server.URL, model, 200)

		_, err := client.GenerateResponse("test prompt", "default")
		if err == nil || !strings.Contains(err.Error(), "empty response from API") {
			t.Errorf("Expected empty response error, got: %v", err)
		}
	})

	t.Run("Malformed JSON Response", func(t *testing.T) {
		malformedResponse := `{"choices":`
		server := mockOpenAIServer(t, http.StatusOK, malformedResponse, apiKey, model)
		defer server.Close()

		client := NewOpenAIClient(apiKey, server.URL, model, 200)

		_, err := client.GenerateResponse("test prompt", "default")
		if err == nil || !strings.Contains(err.Error(), "failed to unmarshal response") {
			t.Errorf("Expected unmarshal error, got: %v", err)
		}
	})
}
