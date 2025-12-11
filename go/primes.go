package main

import (
	"fmt"
	"sync"
)

// Use a mutex to protect our map from concurrent access issues
var primeCache = &sync.Map{}
var mu sync.Mutex // Used for locking when accessing the cache

// Check if a number is prime in a cached manner
func isPrime(n int) bool {
	// Try to get from cache first
	if v, ok := primeCache.Load(n); ok {
		return v.(bool)
	}

	// Cache miss - compute result and store in cache
	mu.Lock()
	if v, ok := primeCache.Load(n); ok {
		mu.Unlock()
		return v.(bool)
	}
	mu.Unlock()

	prime := true // Initial assumption is the number is prime

	// Check divisors up to sqrt(n)
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			prime = false
			break
		}
	}

	mu.Lock() // Lock while storing in the cache
	primeCache.Store(n, prime)
	mu.Unlock()
	return prime
}

func main() {
	// RUN THE PROGRAM FROM COMMAND LINE
	fmt.Println(isPrime(7)) // Should print: true
	fmt.Println(isPrime(8)) // Should print: false
	fmt.Println(isPrime(7)) // Cache hit, should be fast

	var primes []int

	for i := 2; i <= 200; i++ {
		if isPrime(i) {
			primes = append(primes, i)
		}
	}

	fmt.Println("Primes up to 200 with caching:")
	fmt.Println(primes)

	primes = nil

	// Clear the cache and repeat for comparison
	primeCache.Store(nil, "") // Invalidate all elements in primeCache
	fmt.Println("\nPrimes up to 200 without caching:")
	for i := 2; i <= 200; i++ {
		if isPrime(i) {
			primes = append(primes, i)
		}
	}
	fmt.Println(primes)

}
