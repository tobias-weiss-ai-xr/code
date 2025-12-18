package config

import (
	"encoding/json"
	"os"

	"testing"
)

// Helper function to create a temporary config file for testing
func createTempConfigFile(t *testing.T, content string) string {
	tmpfile, err := os.CreateTemp("", "config-test-*.json")
	if err != nil {
		t.Fatalf("Failed to create temporary config file: %v", err)
	}
	defer tmpfile.Close()

	if _, err := tmpfile.WriteString(content); err != nil {
		os.Remove(tmpfile.Name())
		t.Fatalf("Failed to write to temporary config file: %v", err)
	}
	return tmpfile.Name()
}

func TestLoad(t *testing.T) {
	// Clean up environment variables before and after tests
	originalClaudeAPIKey := os.Getenv("CLAUDE_API_KEY")
	originalOpenAIAPIKey := os.Getenv("OPENAI_API_KEY")
	originalAPIProvider := os.Getenv("API_PROVIDER")
	originalOpenAIBaseURL := os.Getenv("OPENAI_BASE_URL")
	originalOllamaModel := os.Getenv("OLLAMA_MODEL")

	defer func() {
		os.Setenv("CLAUDE_API_KEY", originalClaudeAPIKey)
		os.Setenv("OPENAI_API_KEY", originalOpenAIAPIKey)
		os.Setenv("API_PROVIDER", originalAPIProvider)
		os.Setenv("OPENAI_BASE_URL", originalOpenAIBaseURL)
		os.Setenv("OLLAMA_MODEL", originalOllamaModel)
	}()

	os.Unsetenv("CLAUDE_API_KEY")
	os.Unsetenv("OPENAI_API_KEY")
	os.Unsetenv("API_PROVIDER")
	os.Unsetenv("OPENAI_BASE_URL")
	os.Unsetenv("OLLAMA_MODEL")

	t.Run("Load from file success", func(t *testing.T) {
		cfgContent := `{
            "api_provider": "openai",
            "openai_api_key": "test-openai-key",
            "osc_receive_port": 1234,
            "osc_send_port": 5678,
            "max_tokens": 100
        }`
		tmpfile := createTempConfigFile(t, cfgContent)
		defer os.Remove(tmpfile)

		cfg, err := loadFromFile(tmpfile)
		if err != nil {
			t.Fatalf("Load() failed: %v", err)
		}
		if cfg.APIProvider != "openai" || cfg.OpenAIAPIKey != "test-openai-key" || cfg.OSCReceivePort != 1234 {
			t.Errorf("Loaded config mismatch: %+v", cfg)
		}
		// Test defaults for fields not in file
		if cfg.ClaudeModel == "" || cfg.OSCHost == "" {
			t.Errorf("Defaults not applied: %+v", cfg)
		}
	})

	t.Run("Load from file - invalid JSON", func(t *testing.T) {
		cfgContent := `{"api_provider": "openai",` // Invalid JSON
		tmpfile := createTempConfigFile(t, cfgContent)
		defer os.Remove(tmpfile)

		_, err := loadFromFile(tmpfile)
		if err == nil {
			t.Fatal("Load() with invalid JSON did not return an error")
		}
	})

	t.Run("Load from env vars - Claude", func(t *testing.T) {
		os.Setenv("API_PROVIDER", "claude")
		os.Setenv("CLAUDE_API_KEY", "test-claude-key")
		os.Setenv("OSC_RECEIVE_PORT", "8000")
		os.Setenv("OSC_HOST", "192.168.1.1")
		os.Setenv("CLAUDE_MODEL", "test-claude-model") // Added this line

		cfg, err := Load() // Calls the main Load() func
		if err != nil {
			t.Fatalf("Load() failed for env vars: %v", err)
		}
		if cfg.APIProvider != "claude" || cfg.ClaudeAPIKey != "test-claude-key" || cfg.OSCReceivePort != 8000 || cfg.OSCHost != "192.168.1.1" || cfg.ClaudeModel != "test-claude-model" {
			t.Errorf("Loaded config from env vars mismatch: %+v", cfg)
		}
	})

	t.Run("Load from env vars - Ollama with OpenAI URL", func(t *testing.T) {
		os.Setenv("API_PROVIDER", "ollama")
		os.Setenv("OPENAI_BASE_URL", "http://localhost:11434/v1")
		os.Setenv("OLLAMA_MODEL", "llama2")

		cfg, err := Load()
		if err != nil {
			t.Fatalf("Load() failed for env vars: %v", err)
		}
		if cfg.APIProvider != "ollama" || cfg.OpenAIBaseURL != "http://localhost:11434/v1" || cfg.OllamaModel != "llama2" {
			t.Errorf("Loaded config from env vars mismatch: %+v", cfg)
		}
	})

	t.Run("Load from env vars - missing required API_PROVIDER", func(t *testing.T) {
		os.Unsetenv("API_PROVIDER")
		os.Setenv("CLAUDE_API_KEY", "some-key") // Will be defaulted to claude later

		cfg, err := Load()
		if err != nil {
			t.Fatalf("Load() failed for missing API_PROVIDER: %v", err)
		}
		// Should default to claude
		if cfg.APIProvider != "" { // This should be empty until Validate()
			t.Errorf("APIProvider should be empty before Validate(), got: %s", cfg.APIProvider)
		}
		if err := cfg.Validate(); err != nil {
			t.Fatalf("Validate failed for default APIProvider: %v", err)
		}
		if cfg.APIProvider != "claude" {
			t.Errorf("APIProvider not defaulted to 'claude' after Validate(), got: %s", cfg.APIProvider)
		}
	})

	t.Run("Load from env vars - missing API key with claude provider set", func(t *testing.T) {
		os.Setenv("API_PROVIDER", "claude")
		os.Unsetenv("CLAUDE_API_KEY")

		cfg, err := Load()
		if err != nil {
			t.Fatalf("Load() failed: %v", err)
		}
		// Validation should fail here, not Load()
		if err := cfg.Validate(); err == nil {
			t.Error("Validate() did not return an error for missing Claude API key")
		}
	})

	t.Run("Load from env vars - missing OPENAI_API_KEY with openai provider set", func(t *testing.T) {
		os.Setenv("API_PROVIDER", "openai")
		os.Unsetenv("OPENAI_API_KEY")

		cfg, err := Load()
		if err != nil {
			t.Fatalf("Load() failed: %v", err)
		}
		if err := cfg.Validate(); err == nil {
			t.Error("Validate() did not return an error for missing OpenAI API key")
		}
	})

	t.Run("Load from env vars - missing OPENAI_BASE_URL with ollama provider set", func(t *testing.T) {
		os.Setenv("API_PROVIDER", "ollama")
		os.Setenv("OLLAMA_MODEL", "llama3")
		os.Unsetenv("OPENAI_BASE_URL")

		cfg, err := Load()
		if err != nil {
			t.Fatalf("Load() failed: %v", err)
		}
		if err := cfg.Validate(); err == nil {
			t.Error("Validate() did not return an error for missing Ollama base URL")
		}
	})
}

func TestValidate(t *testing.T) {
	t.Run("Valid Claude config", func(t *testing.T) {
		cfg := &Config{
			APIProvider:    "claude",
			ClaudeAPIKey:   "test-key",
			OSCReceivePort: 7400,
			OSCSendPort:    7401,
		}
		if err := cfg.Validate(); err != nil {
			t.Errorf("Valid Claude config failed validation: %v", err)
		}
	})

	t.Run("Invalid Claude config - missing API key", func(t *testing.T) {
		cfg := &Config{
			APIProvider:    "claude",
			OSCReceivePort: 7400,
			OSCSendPort:    7401,
		}
		if err := cfg.Validate(); err == nil {
			t.Error("Invalid Claude config passed validation")
		}
	})

	t.Run("Valid OpenAI config", func(t *testing.T) {
		cfg := &Config{
			APIProvider:    "openai",
			OpenAIAPIKey:   "test-key",
			OSCReceivePort: 7400,
			OSCSendPort:    7401,
		}
		if err := cfg.Validate(); err != nil {
			t.Errorf("Valid OpenAI config failed validation: %v", err)
		}
		if cfg.OpenAIBaseURL == "" { // Check default base URL
			t.Errorf("OpenAIBaseURL not defaulted for OpenAI provider")
		}
	})

	t.Run("Invalid OpenAI config - missing API key", func(t *testing.T) {
		cfg := &Config{
			APIProvider:    "openai",
			OSCReceivePort: 7400,
			OSCSendPort:    7401,
		}
		if err := cfg.Validate(); err == nil {
			t.Error("Invalid OpenAI config passed validation")
		}
	})

	t.Run("Valid Ollama config", func(t *testing.T) {
		cfg := &Config{
			APIProvider:    "ollama",
			OpenAIBaseURL:  "http://localhost:11434/v1",
			OllamaModel:    "llama3",
			OSCReceivePort: 7400,
			OSCSendPort:    7401,
		}
		if err := cfg.Validate(); err != nil {
			t.Errorf("Valid Ollama config failed validation: %v", err)
		}
	})

	t.Run("Invalid Ollama config - missing base URL", func(t *testing.T) {
		cfg := &Config{
			APIProvider:    "ollama",
			OllamaModel:    "llama3",
			OSCReceivePort: 7400,
			OSCSendPort:    7401,
		}
		if err := cfg.Validate(); err == nil {
			t.Error("Invalid Ollama config passed validation (missing base URL)")
		}
	})

	t.Run("Invalid Ollama config - missing model", func(t *testing.T) {
		cfg := &Config{
			APIProvider:    "ollama",
			OpenAIBaseURL:  "http://localhost:11434/v1",
			OSCReceivePort: 7400,
			OSCSendPort:    7401,
		}
		if err := cfg.Validate(); err == nil {
			t.Error("Invalid Ollama config passed validation (missing model)")
		}
	})

	t.Run("Invalid port range - receive", func(t *testing.T) {
		cfg := &Config{
			APIProvider:    "claude",
			ClaudeAPIKey:   "test-key",
			OSCReceivePort: 100, // Invalid
			OSCSendPort:    7401,
		}
		if err := cfg.Validate(); err == nil {
			t.Error("Invalid receive port passed validation")
		}
	})

	t.Run("Invalid port range - send", func(t *testing.T) {
		cfg := &Config{
			APIProvider:    "claude",
			ClaudeAPIKey:   "test-key",
			OSCReceivePort: 7400,
			OSCSendPort:    99999, // Invalid
		}
		if err := cfg.Validate(); err == nil {
			t.Error("Invalid send port passed validation")
		}
	})

	t.Run("Unknown API provider", func(t *testing.T) {
		cfg := &Config{
			APIProvider:    "unknown",
			OSCReceivePort: 7400,
			OSCSendPort:    7401,
		}
		if err := cfg.Validate(); err == nil {
			t.Error("Unknown API provider passed validation")
		}
	})
}

func TestSave(t *testing.T) {
	t.Run("Save to file success", func(t *testing.T) {
		cfg := &Config{
			APIProvider:    "claude",
			ClaudeAPIKey:   "save-key",
			OSCReceivePort: 1234,
			OSCSendPort:    5678,
			OSCHost:        "1.2.3.4",
			ClaudeModel:    "test-model",
			MaxTokens:      500,
			LogFile:        "test.log",
			EnableCache:    true,
			CacheTTL:       600,
		}

		tmpfile, err := os.CreateTemp("", "config-save-*.json")
		if err != nil {
			t.Fatalf("Failed to create temporary save file: %v", err)
		}
		filePath := tmpfile.Name()
		tmpfile.Close() // Close before saving
		defer os.Remove(filePath)

		if err := cfg.Save(filePath); err != nil {
			t.Fatalf("Save() failed: %v", err)
		}

		// Verify content
		loadedCfg := Config{}
		data, err := os.ReadFile(filePath)
		if err != nil {
			t.Fatalf("Failed to read saved file: %v", err)
		}
		if err := json.Unmarshal(data, &loadedCfg); err != nil {
			t.Fatalf("Failed to unmarshal saved file: %v", err)
		}

		if loadedCfg.APIProvider != cfg.APIProvider || loadedCfg.ClaudeAPIKey != cfg.ClaudeAPIKey {
			t.Errorf("Saved config mismatch. Expected: %+v, Got: %+v", cfg, loadedCfg)
		}
	})
}

func TestLoad_Full(t *testing.T) {
	// Simulate current working directory for config.json
	originalWD, _ := os.Getwd()
	tmpDir, err := os.MkdirTemp("", "config_test_wd")
	if err != nil {
		t.Fatalf("Failed to create temp dir: %v", err)
	}
	defer os.RemoveAll(tmpDir)

	os.Chdir(tmpDir)
	defer os.Chdir(originalWD)

	// Test case 1: config.json exists, preferred over env vars
	t.Run("config.json preferred over env vars", func(t *testing.T) {
		os.Setenv("CLAUDE_API_KEY", "env-key")
		content := `{"claude_api_key": "file-key", "api_provider": "claude", "osc_receive_port": 7400, "osc_send_port": 7401}`
		err := os.WriteFile("config.json", []byte(content), 0644)
		if err != nil {
			t.Fatalf("Failed to write config.json: %v", err)
		}

		cfg, err := Load()
		if err != nil {
			t.Fatalf("Load() failed: %v", err)
		}
		if cfg.ClaudeAPIKey != "file-key" {
			t.Errorf("Expected ClaudeAPIKey from file, got %s", cfg.ClaudeAPIKey)
		}
	})

	// Test case 2: no config.json, uses env vars
	t.Run("env vars used when no config.json", func(t *testing.T) {
		os.Remove("config.json") // Clean up from previous test
		os.Setenv("API_PROVIDER", "openai")
		os.Setenv("OPENAI_API_KEY", "env-openai-key")
		os.Setenv("OSC_RECEIVE_PORT", "7400")
		os.Setenv("OSC_SEND_PORT", "7401")

		cfg, err := Load()
		if err != nil {
			t.Fatalf("Load() failed: %v", err)
		}
		if cfg.OpenAIAPIKey != "env-openai-key" || cfg.APIProvider != "openai" {
			t.Errorf("Expected OpenAIAPIKey from env, got %s, provider %s", cfg.OpenAIAPIKey, cfg.APIProvider)
		}
	})

	// Test case 3: neither config.json nor sufficient env vars
	t.Run("validation fails without config.json or env vars", func(t *testing.T) {
		os.Remove("config.json")
		os.Unsetenv("API_PROVIDER")
		os.Unsetenv("CLAUDE_API_KEY")
		os.Unsetenv("OPENAI_API_KEY")
		os.Unsetenv("OPENAI_BASE_URL")
		os.Unsetenv("OLLAMA_MODEL")

		cfg, err := Load() // Will load defaults, API_PROVIDER will be empty
		if err != nil {
			t.Fatalf("Load() failed: %v", err)
		}
		if err := cfg.Validate(); err == nil {
			t.Error("Expected validation error for insufficient config, got none")
		}
	})
}
