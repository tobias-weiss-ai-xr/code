package main

import (
    "fmt"
    "net/http"
)

func main() {
    // Send a GET request to the Google Finance page for Google stock
    resp, err := http.Get("https://www.google.com/finance/quote/GOOG")
    if err != nil {
        fmt.Println("Failed to fetch Google share price:", err)
        return
    }
    defer resp.Body.Close()

    // Check if the request was successful
    if resp.StatusCode != http.StatusOK {
        fmt.Println("Failed to fetch Google share price:", resp.Status)
        return
    }

    // Parse the HTML content
    doc, err := html.Parse(resp.Body)
    if err != nil {
        fmt.Println("Failed to parse HTML:", err)
        return
    }

    // Find the element containing the current Google share price
    sharePriceElement := doc.QuerySelector("#price")
    if sharePriceElement == nil {
        fmt.Println("Failed to find share price element")
        return
    }

    // Extract the current Google share price from the element
    sharePrice := sharePriceElement.Text
    fmt.Println("Current Google share price:", sharePrice)
}
