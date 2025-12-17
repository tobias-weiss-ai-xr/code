package main

import (
    "fmt"
    "log"
    "rsc.io/quote"
    "tobias-weiss.org/greetings"
)


func main() {
    // Setup logger
    log.SetPrefix("greeting: ")
    log.SetFlags(0)

    var i int
    i = 42
    j := 42.0
    var k float32 = 42.0
    fmt.Println("Hello, World!")
    fmt.Println(quote.Go())
    fmt.Printf("i: value %v, type %T\n", i, i)
    fmt.Printf("j: value %v, type %T\n", j, j)
    fmt.Printf("i: value %v, type %T\n", k, k)
    message, err := greetings.Hello("Tobias")
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(message)
}
