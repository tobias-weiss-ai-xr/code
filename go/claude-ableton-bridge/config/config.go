package config

import (
	"encoding/json"
	"fmt"
	"os"
)

type Config struct {
	ClaudeAPIKey   string `json:"claude_api_key"`
	OSCReceivePort int    `json:"osc_receive_port"`
	OSCSendPort    int    `json:"osc_send_port"`
	OSCHost        string `json:"osc_host"`
	ClaudeModel    string `json:"claude_model"`
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
		return cfg, nil
	}

	// Fall back to environment variables
	apiKey := os.Getenv("CLAUDE_API_KEY")
	if apiKey == "" {
		return nil, fmt.Errorf("CLAUDE_API_KEY not set (use config.json or environment variable)")
	}

	return &Config{
		ClaudeAPIKey:   apiKey,
		OSCReceivePort: 7400,
		OSCSendPort:    7401,
		OSCHost:        "127.0.0.1",
		ClaudeModel:    "claude-sonnet-4-20250514",
		MaxTokens:      2000,
		EnableCache:    true,
		CacheTTL:       300, // 5 minutes
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

	// Set defaults if not specified
	if cfg.OSCReceivePort == 0 {
		cfg.OSCReceivePort = 7400
	}
	if cfg.OSCSendPort == 0 {
		cfg.OSCSendPort = 7401
	}
	if cfg.OSCHost == "" {
		cfg.OSCHost = "127.0.0.1"
	}
	if cfg.ClaudeModel == "" {
		cfg.ClaudeModel = "claude-sonnet-4-20250514"
	}
	if cfg.MaxTokens == 0 {
		cfg.MaxTokens = 2000
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
	if c.ClaudeAPIKey == "" {
		return fmt.Errorf("claude_api_key is required")
	}
	if c.OSCReceivePort < 1024 || c.OSCReceivePort > 65535 {
		return fmt.Errorf("osc_receive_port must be between 1024 and 65535")
	}
	if c.OSCSendPort < 1024 || c.OSCSendPort > 65535 {
		return fmt.Errorf("osc_send_port must be between 1024 and 65535")
	}
	return nil
}