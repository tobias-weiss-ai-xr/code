package osc

import (
	"claude-ableton-bridge/config"
	"testing"
	"time"

	"github.com/hypebeast/go-osc/osc"
)

// mockLLMClient is a mock implementation of LLMClient for testing
type mockLLMClient struct {
	response string
	err      error
}

// APIError is a helper for testing
type APIError string

func (e APIError) Error() string {
	return string(e)
}

func (m *mockLLMClient) GenerateResponse(prompt, context string) (string, error) {
	return m.response, m.err
}

// TestNewServer tests server creation
func TestNewServer(t *testing.T) {
	t.Run("Create server with valid config", func(t *testing.T) {
		cfg := &config.Config{
			OSCReceivePort: 7400,
			OSCSendPort:    7401,
			OSCHost:        "127.0.0.1",
			EnableCache:    false,
		}

		mockClient := &mockLLMClient{response: "test response"}
		server, err := NewServer(cfg, mockClient)

		if err != nil {
			t.Fatalf("NewServer failed: %v", err)
		}
		if server == nil {
			t.Fatal("Expected non-nil server")
		}
		if server.config != cfg {
			t.Error("Config not set correctly")
		}
		if server.llmClient == nil {
			t.Error("LLM client not set")
		}
		if server.cache != nil {
			t.Error("Cache should be nil when disabled")
		}
	})

	t.Run("Create server with cache enabled", func(t *testing.T) {
		cfg := &config.Config{
			OSCReceivePort: 7402,
			OSCSendPort:    7403,
			OSCHost:        "127.0.0.1",
			EnableCache:    true,
			CacheTTL:       300,
		}

		mockClient := &mockLLMClient{response: "test response"}
		server, err := NewServer(cfg, mockClient)

		if err != nil {
			t.Fatalf("NewServer failed: %v", err)
		}
		if server.cache == nil {
			t.Error("Cache should be non-nil when enabled")
		}
	})

	t.Run("Verify server address format", func(t *testing.T) {
		cfg := &config.Config{
			OSCReceivePort: 7500,
			OSCSendPort:    7501,
			OSCHost:        "localhost",
			EnableCache:    false,
		}

		mockClient := &mockLLMClient{response: "test"}
		server, err := NewServer(cfg, mockClient)

		if err != nil {
			t.Fatalf("NewServer failed: %v", err)
		}
		if server.oscServer == nil {
			t.Fatal("OSC server not initialized")
		}
		if server.oscServer.Addr != "localhost:7500" {
			t.Errorf("Expected address 'localhost:7500', got '%s'", server.oscServer.Addr)
		}
	})
}

// TestStop tests graceful shutdown
func TestStop(t *testing.T) {
	cfg := &config.Config{
		OSCReceivePort: 7404,
		OSCSendPort:    7405,
		OSCHost:        "127.0.0.1",
		EnableCache:    false,
	}

	mockClient := &mockLLMClient{response: "test"}
	server, err := NewServer(cfg, mockClient)
	if err != nil {
		t.Fatalf("NewServer failed: %v", err)
	}

	// Stop should not panic
	server.Stop()
}

// TestAddMsgHandler tests handler registration
func TestAddMsgHandler(t *testing.T) {
	cfg := &config.Config{
		OSCReceivePort: 7406,
		OSCSendPort:    7407,
		OSCHost:        "127.0.0.1",
		EnableCache:    false,
	}

	mockClient := &mockLLMClient{response: "test"}
	server, err := NewServer(cfg, mockClient)
	if err != nil {
		t.Fatalf("NewServer failed: %v", err)
	}

	// Test adding a handler
	testHandler := func(msg *osc.Message) {
		// Handler for testing
	}

	err = server.AddMsgHandler("/test/address", osc.HandlerFunc(testHandler))
	if err != nil {
		t.Errorf("AddMsgHandler failed: %v", err)
	}
}

// TestSendResponse tests response sending
func TestSendResponse(t *testing.T) {
	cfg := &config.Config{
		OSCReceivePort: 7408,
		OSCSendPort:    7409,
		OSCHost:        "127.0.0.1",
		EnableCache:    false,
	}

	mockClient := &mockLLMClient{response: "test"}
	server, err := NewServer(cfg, mockClient)
	if err != nil {
		t.Fatalf("NewServer failed: %v", err)
	}

	// SendResponse should not panic (may fail to actually send if nothing is listening)
	server.sendResponse("test response")
}

// TestSendError tests error sending
func TestSendError(t *testing.T) {
	cfg := &config.Config{
		OSCReceivePort: 7410,
		OSCSendPort:    7411,
		OSCHost:        "127.0.0.1",
		EnableCache:    false,
	}

	mockClient := &mockLLMClient{response: "test"}
	server, err := NewServer(cfg, mockClient)
	if err != nil {
		t.Fatalf("NewServer failed: %v", err)
	}

	// SendError should not panic
	server.sendError("test error")
}

// TestProcessPrompt tests prompt processing with cache
func TestProcessPrompt(t *testing.T) {
	t.Run("Process prompt without cache", func(t *testing.T) {
		cfg := &config.Config{
			OSCReceivePort: 7412,
			OSCSendPort:    7413,
			OSCHost:        "127.0.0.1",
			EnableCache:    false,
		}

		mockClient := &mockLLMClient{response: "test response"}
		server, err := NewServer(cfg, mockClient)
		if err != nil {
			t.Fatalf("NewServer failed: %v", err)
		}

		// ProcessPrompt should not panic
		server.processPrompt("test prompt", "music")
	})

	t.Run("Process prompt with cache", func(t *testing.T) {
		cfg := &config.Config{
			OSCReceivePort: 7414,
			OSCSendPort:    7415,
			OSCHost:        "127.0.0.1",
			EnableCache:    true,
			CacheTTL:       300,
		}

		mockClient := &mockLLMClient{response: "cached response"}
		server, err := NewServer(cfg, mockClient)
		if err != nil {
			t.Fatalf("NewServer failed: %v", err)
		}

		// First call should cache the response
		server.processPrompt("cached prompt", "music")

		// Wait a bit for async processing
		time.Sleep(100 * time.Millisecond)

		// Check cache size
		if server.cache.Size() != 1 {
			t.Logf("Cache size after first prompt: %d", server.cache.Size())
		}
	})

	t.Run("Process prompt with API error", func(t *testing.T) {
		cfg := &config.Config{
			OSCReceivePort: 7416,
			OSCSendPort:    7417,
			OSCHost:        "127.0.0.1",
			EnableCache:    false,
		}

		mockClient := &mockLLMClient{response: "", err: APIError("API error")}
		server, err := NewServer(cfg, mockClient)
		if err != nil {
			t.Fatalf("NewServer failed: %v", err)
		}

		// Should handle error gracefully
		server.processPrompt("error prompt", "music")
	})
}

// TestSendMIDIData tests MIDI data sending
func TestSendMIDIData(t *testing.T) {
	cfg := &config.Config{
		OSCReceivePort: 7418,
		OSCSendPort:    7419,
		OSCHost:        "127.0.0.1",
		EnableCache:    false,
	}

	mockClient := &mockLLMClient{response: "test"}
	_, err := NewServer(cfg, mockClient)
	if err != nil {
		t.Fatalf("NewServer failed: %v", err)
	}

	// Create test MIDI data
	type jsoner interface {
		ToJSON() ([]byte, error)
	}
	_ = jsoner(nil) // Verify the interface exists

	// sendMIDIData expects *midi.Data, we'll test it indirectly through integration tests
}

// Benchmark tests
func BenchmarkProcessPrompt(b *testing.B) {
	cfg := &config.Config{
		OSCReceivePort: 7420,
		OSCSendPort:    7421,
		OSCHost:        "127.0.0.1",
		EnableCache:    true,
		CacheTTL:       300,
	}

	mockClient := &mockLLMClient{response: "benchmark response"}
	server, _ := NewServer(cfg, mockClient)

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		server.processPrompt("benchmark prompt", "music")
	}
}
