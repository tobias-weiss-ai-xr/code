package cache

import (
	"sync"
	"testing"
	"time"
)

// Test NewCache creation
func TestNewCache(t *testing.T) {
	t.Run("Create cache with valid TTL", func(t *testing.T) {
		ttl := 5 * time.Minute
		cache := NewCache(ttl)

		if cache == nil {
			t.Fatal("NewCache returned nil")
		}
		if cache.ttl != ttl {
			t.Errorf("Expected TTL %v, got %v", ttl, cache.ttl)
		}
		if cache.store == nil {
			t.Error("Cache store is not initialized")
		}
	})

	t.Run("Create cache with zero TTL", func(t *testing.T) {
		cache := NewCache(0)

		if cache == nil {
			t.Fatal("NewCache returned nil")
		}
		if cache.ttl != 0 {
			t.Errorf("Expected TTL 0, got %v", cache.ttl)
		}
	})

	t.Run("Create cache with negative TTL", func(t *testing.T) {
		cache := NewCache(-1 * time.Minute)

		if cache == nil {
			t.Fatal("NewCache returned nil")
		}
	})
}

// Test Set/Get operations
func TestSetGet(t *testing.T) {
	t.Run("Set and Get existing key", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)
		key := "test-key"
		value := "test-value"

		cache.Set(key, value)
		retrieved, exists := cache.Get(key)

		if !exists {
			t.Error("Expected key to exist")
		}
		if retrieved != value {
			t.Errorf("Expected value '%s', got '%s'", value, retrieved)
		}
	})

	t.Run("Get non-existing key", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)
		_, exists := cache.Get("non-existing")

		if exists {
			t.Error("Expected non-existing key to not exist")
		}
	})

	t.Run("Set updates existing key", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)
		key := "test-key"
		value1 := "value-1"
		value2 := "value-2"

		cache.Set(key, value1)
		cache.Set(key, value2)
		retrieved, _ := cache.Get(key)

		if retrieved != value2 {
			t.Errorf("Expected updated value '%s', got '%s'", value2, retrieved)
		}
	})

	t.Run("Empty key and value", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)

		cache.Set("", "")
		retrieved, exists := cache.Get("")

		if !exists {
			t.Error("Expected empty key to exist")
		}
		if retrieved != "" {
			t.Errorf("Expected empty value, got '%s'", retrieved)
		}
	})
}

// Test Get with expired entries
func TestGetExpired(t *testing.T) {
	t.Run("Expired entry not returned", func(t *testing.T) {
		cache := NewCache(10 * time.Millisecond)
		key := "expiring-key"
		value := "expiring-value"

		cache.Set(key, value)

		// Wait for expiration
		time.Sleep(15 * time.Millisecond)

		_, exists := cache.Get(key)
		if exists {
			t.Error("Expected expired entry to not exist")
		}
	})

	t.Run("Entry available before expiration", func(t *testing.T) {
		cache := NewCache(100 * time.Millisecond)
		key := "key"
		value := "value"

		cache.Set(key, value)

		// Immediately retrieve - should exist
		retrieved, exists := cache.Get(key)
		if !exists {
			t.Error("Expected entry to exist immediately after Set")
		}
		if retrieved != value {
			t.Errorf("Expected '%s', got '%s'", value, retrieved)
		}

		// Wait half of TTL - should still exist
		time.Sleep(50 * time.Millisecond)
		_, exists = cache.Get(key)
		if !exists {
			t.Error("Expected entry to exist before TTL expires")
		}
	})

	t.Run("Zero TTL means immediate expiration", func(t *testing.T) {
		cache := NewCache(0)
		key := "zero-ttl-key"
		value := "value"

		cache.Set(key, value)

		// With zero TTL, entry should be considered expired immediately
		time.Sleep(1 * time.Millisecond)
		_, exists := cache.Get(key)
		if exists {
			t.Error("Expected zero TTL entry to be expired")
		}
	})
}

// Test Hash generation for different inputs
func TestHash(t *testing.T) {
	t.Run("Same input produces same hash", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)
		prompt := "test prompt"
		context := "test context"

		hash1 := cache.Hash(prompt, context)
		hash2 := cache.Hash(prompt, context)

		if hash1 != hash2 {
			t.Error("Same input should produce same hash")
		}
	})

	t.Run("Different prompt produces different hash", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)
		context := "context"

		hash1 := cache.Hash("prompt1", context)
		hash2 := cache.Hash("prompt2", context)

		if hash1 == hash2 {
			t.Error("Different prompts should produce different hashes")
		}
	})

	t.Run("Different context produces different hash", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)
		prompt := "prompt"

		hash1 := cache.Hash(prompt, "context1")
		hash2 := cache.Hash(prompt, "context2")

		if hash1 == hash2 {
			t.Error("Different contexts should produce different hashes")
		}
	})

	t.Run("Empty prompt and context", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)

		hash := cache.Hash("", "")
		if hash == "" {
			t.Error("Hash should not be empty for empty input")
		}
	})

	t.Run("Hash format is valid SHA256", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)

		hash := cache.Hash("test", "context")
		// SHA256 hex encoding should be 64 characters
		if len(hash) != 64 {
			t.Errorf("Expected hash length 64, got %d", len(hash))
		}
	})
}

// Test Clear operation
func TestClear(t *testing.T) {
	t.Run("Clear removes all entries", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)

		// Add multiple entries
		for i := 0; i < 5; i++ {
			cache.Set(string(rune('a'+i)), string(rune('A'+i)))
		}

		if cache.Size() != 5 {
			t.Errorf("Expected size 5 before clear, got %d", cache.Size())
		}

		cache.Clear()

		if cache.Size() != 0 {
			t.Errorf("Expected size 0 after clear, got %d", cache.Size())
		}

		// Verify no entries exist
		for i := 0; i < 5; i++ {
			_, exists := cache.Get(string(rune('a' + i)))
			if exists {
				t.Error("Expected no entries after clear")
			}
		}
	})

	t.Run("Clear on empty cache", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)

		cache.Clear() // Should not panic

		if cache.Size() != 0 {
			t.Errorf("Expected size 0, got %d", cache.Size())
		}
	})

	t.Run("Can add entries after clear", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)

		cache.Set("key1", "value1")
		cache.Clear()
		cache.Set("key2", "value2")

		retrieved, exists := cache.Get("key2")
		if !exists || retrieved != "value2" {
			t.Error("Expected to add entries after clear")
		}
	})
}

// Test Size operation
func TestSize(t *testing.T) {
	t.Run("Size of empty cache", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)
		if cache.Size() != 0 {
			t.Errorf("Expected size 0 for empty cache, got %d", cache.Size())
		}
	})

	t.Run("Size increases with entries", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)

		for i := 1; i <= 10; i++ {
			cache.Set(string(rune('0'+i)), "value")
			if cache.Size() != i {
				t.Errorf("Expected size %d, got %d", i, cache.Size())
			}
		}
	})

	t.Run("Size unaffected by updating existing key", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)

		cache.Set("key", "value1")
		size1 := cache.Size()

		cache.Set("key", "value2")
		size2 := cache.Size()

		if size1 != size2 {
			t.Errorf("Size should not change when updating key: %d vs %d", size1, size2)
		}
	})
}

// Test Concurrent access (thread safety)
func TestConcurrentAccess(t *testing.T) {
	t.Run("Concurrent writes", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)
		numGoroutines := 100
		writesPerGoroutine := 10

		var wg sync.WaitGroup
		wg.Add(numGoroutines)

		for i := 0; i < numGoroutines; i++ {
			go func(id int) {
				defer wg.Done()
				for j := 0; j < writesPerGoroutine; j++ {
					key := string(rune('a' + (id % 26)))
					value := string(rune('A' + id))
					cache.Set(key, value)
				}
			}(i)
		}

		wg.Wait()

		// Should have at most 26 unique keys
		if cache.Size() > 26 {
			t.Errorf("Expected at most 26 unique keys, got %d", cache.Size())
		}
	})

	t.Run("Concurrent reads", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)
		cache.Set("key", "value")

		numGoroutines := 100
		readsPerGoroutine := 100

		var wg sync.WaitGroup
		wg.Add(numGoroutines)

		for i := 0; i < numGoroutines; i++ {
			go func() {
				defer wg.Done()
				for j := 0; j < readsPerGoroutine; j++ {
					cache.Get("key")
				}
			}()
		}

		wg.Wait()

		// Verify the value still exists and is correct
		retrieved, exists := cache.Get("key")
		if !exists || retrieved != "value" {
			t.Error("Concurrent reads corrupted cache state")
		}
	})

	t.Run("Concurrent writes and reads", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)
		numWriters := 50
		numReaders := 50

		var wg sync.WaitGroup
		wg.Add(numWriters + numReaders)

		// Initialize with some data
		cache.Set("initial", "value")

		// Writers
		for i := 0; i < numWriters; i++ {
			go func(id int) {
				defer wg.Done()
				key := string(rune('a' + (id % 26)))
				cache.Set(key, "value")
			}(i)
		}

		// Readers
		for i := 0; i < numReaders; i++ {
			go func() {
				defer wg.Done()
				cache.Get("initial")
			}()
		}

		wg.Wait()

		// Should not panic or deadlock
	})

	t.Run("Concurrent clears", func(t *testing.T) {
		cache := NewCache(1 * time.Hour)
		numGoroutines := 10

		// Populate cache
		for i := 0; i < 100; i++ {
			cache.Set(string(rune('0'+i%10)), "value")
		}

		var wg sync.WaitGroup
		wg.Add(numGoroutines)

		for i := 0; i < numGoroutines; i++ {
			go func() {
				defer wg.Done()
				cache.Clear()
			}()
		}

		wg.Wait()

		// Cache should be empty
		if cache.Size() != 0 {
			t.Errorf("Expected empty cache after concurrent clears, got size %d", cache.Size())
		}
	})
}
