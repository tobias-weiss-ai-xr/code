package cache

import (
	"crypto/sha256"
	"encoding/hex"
	"sync"
	"time"
)

type Cache struct {
	store map[string]cacheEntry
	mu    sync.RWMutex
	ttl   time.Duration
}

type cacheEntry struct {
	value     string
	timestamp time.Time
}

// NewCache creates a new cache with specified TTL
func NewCache(ttl time.Duration) *Cache {
	c := &Cache{
		store: make(map[string]cacheEntry),
		ttl:   ttl,
	}

	// Start cleanup goroutine
	go c.cleanup()

	return c
}

// Get retrieves a value from cache if it exists and hasn't expired
func (c *Cache) Get(key string) (string, bool) {
	c.mu.RLock()
	defer c.mu.RUnlock()

	entry, exists := c.store[key]
	if !exists {
		return "", false
	}

	if time.Since(entry.timestamp) > c.ttl {
		return "", false
	}

	return entry.value, true
}

// Set stores a value in cache
func (c *Cache) Set(key, value string) {
	c.mu.Lock()
	defer c.mu.Unlock()

	c.store[key] = cacheEntry{
		value:     value,
		timestamp: time.Now(),
	}
}

// Hash creates a cache key from prompt and context
func (c *Cache) Hash(prompt, context string) string {
	h := sha256.New()
	h.Write([]byte(prompt + ":" + context))
	return hex.EncodeToString(h.Sum(nil))
}

// Clear removes all entries from cache
func (c *Cache) Clear() {
	c.mu.Lock()
	defer c.mu.Unlock()

	c.store = make(map[string]cacheEntry)
}

// Size returns the number of entries in cache
func (c *Cache) Size() int {
	c.mu.RLock()
	defer c.mu.RUnlock()

	return len(c.store)
}

// cleanup periodically removes expired entries
func (c *Cache) cleanup() {
	ticker := time.NewTicker(5 * time.Minute)
	defer ticker.Stop()

	for range ticker.C {
		c.mu.Lock()
		for key, entry := range c.store {
			if time.Since(entry.timestamp) > c.ttl {
				delete(c.store, key)
			}
		}
		c.mu.Unlock()
	}
}