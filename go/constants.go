package main

import (
	"fmt"
	"math"
)

const s string = "constant"

// main is the entry point of the program
func main() {
	// Print the constant string
	fmt.Println(s)

	// Define a constant for the number of iterations
	const n = 500000

	// Calculate the value of d
	// This is used to calculate the sine of n
	const d = 3e20 / n

	// Print the value of d
	fmt.Println(d)

	// Print the value of d converted to an int64
	fmt.Println(int64(d))

	// Print the sine of n
	fmt.Println(math.Sin(n))
}
