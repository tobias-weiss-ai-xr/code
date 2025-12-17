package performance

import (
	"database/sql"
	"fmt"
	"log"
	"time"
)

// getStockPerformance calculates the 3, 6, 12, and n-month performance for all shares.
func GetStockPerformance(db *sql.DB, symbols []string, nMonths int) (map[string]map[string]float64, error) {
	performance := make(map[string]map[string]float64)

	for _, symbol := range symbols {
		// Fetch historical data for the symbol
		rows, err := db.Query("SELECT price, timestamp FROM stocks WHERE symbol = ? ORDER BY timestamp ASC", symbol)
		if err != nil {
			log.Printf("Error fetching historical data for %s: %v", symbol, err)
			continue
		}
		defer rows.Close()

		var prices []struct {
			Price     float64
			Timestamp time.Time
		}
		for rows.Next() {
			var pScanned struct {
				Price        float64
				TimestampStr string // Scan into string first
			}
			if err := rows.Scan(&pScanned.Price, &pScanned.TimestampStr); err != nil {
				log.Printf("Error scanning historical data for %s: %v", symbol, err)
				continue
			}
			parsedTime, err := time.Parse("2006-01-02 15:04:05", pScanned.TimestampStr)
			if err != nil {
				log.Printf("Error parsing timestamp for %s: %v", symbol, err)
				continue
			}
			prices = append(prices, struct {
				Price     float64
				Timestamp time.Time
			}{Price: pScanned.Price, Timestamp: parsedTime})
		}

		if len(prices) < 2 {
			log.Printf("Not enough historical data for %s to calculate performance", symbol)
			continue
		}

		symbolPerformance := make(map[string]float64)

		// Calculate performance for different periods
		periods := []int{3, 6, 12, nMonths}
		latestPrice := prices[len(prices)-1].Price

		for _, month := range periods {
			// Find the start date for the period
			startDate := time.Now().AddDate(0, -month, 0)

			// Find the price closest to the start date
			var startPrice float64
			foundStartPrice := false
			for i := len(prices) - 1; i >= 0; i-- {
				if prices[i].Timestamp.Before(startDate) {
					startPrice = prices[i].Price
					foundStartPrice = true
					break
				}
			}

			if !foundStartPrice || startPrice == 0 {
				log.Printf("Not enough data for %d-month performance for %s", month, symbol)
				symbolPerformance[fmt.Sprintf("%d_month_performance", month)] = 0.0 // Indicate no performance
				continue
			}

			// Calculate performance
			perf := ((latestPrice - startPrice) / startPrice) * 100
			symbolPerformance[fmt.Sprintf("%d_month_performance", month)] = perf
		}
		performance[symbol] = symbolPerformance
	}

	return performance, nil
}