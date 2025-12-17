package main

import (
	"fmt"
	"log"
	"os"
	"os/signal"
	"syscall"

	"claude-ableton-bridge/claude"
	"claude-ableton-bridge/config"
	"claude-ableton-bridge/osc"
)

func main() {
	fmt.Println("Claude-Ableton Bridge")
	fmt.Println("====================")

	// Load configuration
	cfg, err := config.Load()
	if err != nil {
		log.Fatalf("Failed to load config: %v", err)
	}

	// Validate configuration
	if err := cfg.Validate(); err != nil {
		log.Fatalf("Invalid configuration: %v", err)
	}

	// Setup logging
	if cfg.LogFile != "" {
		setupLogging(cfg.LogFile)
	}

	log.Println("Configuration loaded successfully")
	log.Printf("Model: %s", cfg.ClaudeModel)
	log.Printf("Cache: %v", cfg.EnableCache)

	// Initialize Claude client
	claudeClient := claude.NewClient(cfg.ClaudeAPIKey)
	log.Println("Claude client initialized")

	// Initialize OSC server
	oscServer, err := osc.NewServer(cfg, claudeClient)
	if err != nil {
		log.Fatalf("Failed to create OSC server: %v", err)
	}

	// Start OSC server in goroutine
	go func() {
		if err := oscServer.Start(); err != nil {
			log.Fatalf("Failed to start OSC server: %v", err)
		}
	}()

	fmt.Printf("\n✓ Bridge running\n")
	fmt.Printf("  Listening on port %d\n", cfg.OSCReceivePort)
	fmt.Printf("  Sending to port %d\n", cfg.OSCSendPort)
	fmt.Printf("  Press Ctrl+C to exit\n\n")

	// Wait for interrupt signal
	sigChan := make(chan os.Signal, 1)
	signal.Notify(sigChan, os.Interrupt, syscall.SIGTERM)
	<-sigChan

	fmt.Println("\nShutting down gracefully...")
	oscServer.Stop()
	fmt.Println("Bridge stopped")
}

func setupLogging(logFile string) {
	f, err := os.OpenFile(logFile, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Printf("Warning: Could not open log file: %v", err)
		return
	}
	log.SetOutput(f)
}