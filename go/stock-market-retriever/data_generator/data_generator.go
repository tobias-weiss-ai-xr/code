package data_generator

import (
	"fmt"
	"log"
	"math/rand"
	"time"
)

// Stock represents a stock quote.
type Stock struct {
	Symbol           string
	Name             string
	Price            float64
	Change           float64
	ChangePercent    float64
	DayHigh          float64
	DayLow           float64
	YearHigh         float64
	YearLow          float64
	Volume           int
	FiftyTwoWeekHigh float64
	FiftyTwoWeekLow  float64
	Timestamp        time.Time
}

// fetchStockData fetches stock data for the given symbols.
func FetchStockData(symbols []string) ([]Stock, error) {
	var allStocks []Stock
	rand.Seed(time.Now().UnixNano()) // Seed the random number generator

	for _, symbol := range symbols {
		log.Printf("Generating historical dummy data for symbol: %s", symbol)
		basePrice := 100.00 + float64(len(symbol))
		currentDate := time.Now()

		// Generate data for the last 2 years and a bit (approx 750 days)
		for i := 0; i < 750; i++ {
			day := currentDate.AddDate(0, 0, -i) // Go back in time

			// Simulate price variation
			price := basePrice + rand.Float64()*10 - 5 // price +/- 5 from base
			if price < 1.0 { // Ensure price doesn't go below 1
				price = 1.0
			}

			dummyStock := Stock{
				Symbol:           symbol,
				Name:             fmt.Sprintf("Dummy Name for %s", symbol),
				Price:            price,
				Change:           rand.Float64()*2 - 1, // Change +/- 1
				ChangePercent:    rand.Float64()*0.02 - 0.01, // Change percent +/- 1%
				DayHigh:          price + rand.Float64()*0.5,
				DayLow:           price - rand.Float64()*0.5,
				YearHigh:         basePrice + 15,
				YearLow:          basePrice - 15,
				Volume:           1000000 + rand.Intn(500000),
				FiftyTwoWeekHigh: basePrice + 15,
				FiftyTwoWeekLow:  basePrice - 15,
				Timestamp:        day,
			}
			allStocks = append(allStocks, dummyStock)
		}
	}
	return allStocks, nil
}