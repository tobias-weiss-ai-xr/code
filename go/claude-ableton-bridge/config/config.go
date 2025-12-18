package config

import (
	"encoding/json"
	"fmt"
	"os"
	"strconv"
)

type Config struct {
	APIProvider    string `json:"api_provider"`
	ClaudeAPIKey   string `json:"claude_api_key,omitempty"`
	OpenAIAPIKey   string `json:"openai_api_key,omitempty"`
	OpenAIBaseURL  string `json:"openai_base_url,omitempty"`
	OllamaModel    string `json:"ollama_model,omitempty"`
	OSCReceivePort int    `json:"osc_receive_port"`
	OSCSendPort    int    `json:"osc_send_port"`
	OSCHost        string `json:"osc_host"`
	ClaudeModel    string `json:"claude_model,omitempty"`
	MaxTokens      int    `json:"max_tokens"`
	LogFile        string `json:"log_file,omitempty"`
	EnableCache    bool   `json:"enable_cache"`
	CacheTTL       int    `json:"cache_ttl_seconds"`
}

// Load configuration from file or environment
func Load() (*Config, error) {
	// Try config file first
	cfg, err := loadFromFile("config.json")
	if err == nil {
		// Set defaults for newly added fields if not present in config.json
		if cfg.APIProvider == "" {
			cfg.APIProvider = "claude"
		}
		if cfg.ClaudeModel == "" {
			cfg.ClaudeModel = "claude-sonnet-4-20250514"
		}
		if cfg.OpenAIBaseURL == "" {
			cfg.OpenAIBaseURL = "https://api.openai.com/v1"
		}
		if cfg.OllamaModel == "" {
			cfg.OllamaModel = "llama3"
		}
		if cfg.MaxTokens == 0 {
			cfg.MaxTokens = 2000
		}
		if cfg.OSCReceivePort == 0 {
			cfg.OSCReceivePort = 7400
		}
		if cfg.OSCSendPort == 0 {
			cfg.OSCSendPort = 7401
		}
		if cfg.OSCHost == "" {
			cfg.OSCHost = "127.0.0.1"
		}
		if cfg.CacheTTL == 0 {
			cfg.CacheTTL = 300
		}
		return cfg, nil
	}

	// Fall back to environment variables and set defaults
	oscReceivePort := 7400
	if pStr := os.Getenv("OSC_RECEIVE_PORT"); pStr != "" {
		if p, err := strconv.Atoi(pStr); err == nil {
			oscReceivePort = p
		}
	}
	oscSendPort := 7401
	if pStr := os.Getenv("OSC_SEND_PORT"); pStr != "" {
		if p, err := strconv.Atoi(pStr); err == nil {
			oscSendPort = p
		}
	}

	maxTokens := 2000
	if mtStr := os.Getenv("MAX_TOKENS"); mtStr != "" {
		if mt, err := strconv.Atoi(mtStr); err == nil {
			maxTokens = mt
		}
	}

	enableCache := true
	if ecStr := os.Getenv("ENABLE_CACHE"); ecStr != "" {
		if ec, err := strconv.ParseBool(ecStr); err == nil {
			enableCache = ec
		}
	}

	cacheTTL := 300
	if ctStr := os.Getenv("CACHE_TTL_SECONDS"); ctStr != "" {
		if ct, err := strconv.Atoi(ctStr); err == nil {
			cacheTTL = ct
		}
	}

	return &Config{
		APIProvider:    os.Getenv("API_PROVIDER"),
		ClaudeAPIKey:   os.Getenv("CLAUDE_API_KEY"),
		OpenAIAPIKey:   os.Getenv("OPENAI_API_KEY"),
		OpenAIBaseURL:  os.Getenv("OPENAI_BASE_URL"),
		OllamaModel:    os.Getenv("OLLAMA_MODEL"),
		OSCReceivePort: oscReceivePort,
		OSCSendPort:    oscSendPort,
		OSCHost:        os.Getenv("OSC_HOST"),
		ClaudeModel:    os.Getenv("CLAUDE_MODEL"),
		MaxTokens:      maxTokens,
		EnableCache:    enableCache,
		CacheTTL:       cacheTTL,
	}, nil
}


func loadFromFile(path string) (*Config, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var cfg Config
	decoder := json.NewDecoder(file)
	if err := decoder.Decode(&cfg); err != nil {
		return nil, err
	}

	// Apply defaults if not specified in file
	if cfg.APIProvider == "" {
		cfg.APIProvider = "claude"
	}
	if cfg.ClaudeModel == "" {
		cfg.ClaudeModel = "claude-sonnet-4-20250514"
	}
	if cfg.OpenAIBaseURL == "" {
		cfg.OpenAIBaseURL = "https://api.openai.com/v1"
	}
	if cfg.OllamaModel == "" {
		cfg.OllamaModel = "llama3"
	}
	if cfg.MaxTokens == 0 {
		cfg.MaxTokens = 2000
	}
	if cfg.OSCReceivePort == 0 {
		cfg.OSCReceivePort = 7400
	}
	if cfg.OSCSendPort == 0 {
		cfg.OSCSendPort = 7401
	}
	if cfg.OSCHost == "" {
		cfg.OSCHost = "127.0.0.1"
	}
	if cfg.CacheTTL == 0 {
		cfg.CacheTTL = 300
	}

	return &cfg, nil
}

// Save configuration to file
func (c *Config) Save(path string) error {
	file, err := os.Create(path)
	if err != nil {
		return err
	}
	defer file.Close()

	encoder := json.NewEncoder(file)
	encoder.SetIndent("", "  ")
	return encoder.Encode(c)
}

// Validate checks if configuration is valid
func (c *Config) Validate() error {
	if c.APIProvider == "" {
		c.APIProvider = "claude" // Default API provider
	}

	switch c.APIProvider {
	case "claude":
		if c.ClaudeAPIKey == "" {
			return fmt.Errorf("claude_api_key is required when API_PROVIDER is 'claude'")
		}
	case "openai":
		if c.OpenAIAPIKey == "" {
			return fmt.Errorf("openai_api_key is required when API_PROVIDER is 'openai'")
		}
		if c.OpenAIBaseURL == "" {
			c.OpenAIBaseURL = "https://api.openai.com/v1" // Default for OpenAI
		}
	case "ollama":
		if c.OpenAIBaseURL == "" { // Ollama uses OpenAI-compatible API base URL
			return fmt.Errorf("openai_base_url (Ollama API base URL) is required when API_PROVIDER is 'ollama'")
		}
		if c.OllamaModel == "" {
			return fmt.Errorf("ollama_model is required when API_PROVIDER is 'ollama'")
		}
	default:
		return fmt.Errorf("unsupported API_PROVIDER: %s. Must be 'claude', 'openai', or 'ollama'", c.APIProvider)
	}

	if c.OSCReceivePort < 1024 || c.OSCReceivePort > 65535 {
		return fmt.Errorf("osc_receive_port must be between 1024 and 65535")
	}
	if c.OSCSendPort < 1024 || c.OSCSendPort > 65535 {
		return fmt.Errorf("osc_send_port must be between 1024 and 65535")
	}
	return nil
}