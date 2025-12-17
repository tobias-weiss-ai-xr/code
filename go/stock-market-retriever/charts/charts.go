package charts

import (
	"database/sql"
	"fmt"
	"image/color"
	"log"
	"time"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
)

// calculateSMA calculates the Simple Moving Average for a given window.
func calculateSMA(prices []float64, window int) []float64 {
	if len(prices) < window {
		return make([]float64, len(prices)) // Return all zeros if not enough data
	}
	sma := make([]float64, len(prices)-window+1)
	for i := 0; i <= len(prices)-window; i++ {
		sum := 0.0
		for j := 0; j < window; j++ {
			sum += prices[i+j]
		}
		sma[i] = sum / float64(window)
	}
	// Pad the beginning with zeros to match the length of the original prices slice
	paddedSMA := make([]float64, len(prices))
	copy(paddedSMA[window-1:], sma)
	return paddedSMA
}

// generateStockPriceChart generates a PNG chart of historical stock prices for a given symbol,
// including 50-day and 200-day Moving Averages.
func GenerateStockPriceChart(db *sql.DB, symbol string, filename string) error {
	rows, err := db.Query("SELECT price, timestamp FROM stocks WHERE symbol = ? ORDER BY timestamp ASC", symbol)
	if err != nil {
		return fmt.Errorf("error fetching historical data for %s: %v", symbol, err)
	}
	defer rows.Close()

	var rawPrices []float64
	var timestamps []time.Time
	pts := make(plotter.XYs, 0)

	for rows.Next() {
		var pScanned struct {
			Price        float64
			TimestampStr string
		}
		if err := rows.Scan(&pScanned.Price, &pScanned.TimestampStr); err != nil {
			return fmt.Errorf("error scanning historical data for %s: %v", symbol, err)
		}
		parsedTime, err := time.Parse("2006-01-02 15:04:05", pScanned.TimestampStr)
		if err != nil {
			return fmt.Errorf("error parsing timestamp for %s: %v", symbol, err)
		}

		rawPrices = append(rawPrices, pScanned.Price)
		timestamps = append(timestamps, parsedTime)
		pts = append(pts, plotter.XY{X: float64(parsedTime.Unix()), Y: pScanned.Price})
	}

	if len(pts) == 0 {
		return fmt.Errorf("no historical data found for %s to generate chart", symbol)
	}

	p := plot.New()

	p.Title.Text = fmt.Sprintf("%s Stock Price History", symbol)
	p.X.Label.Text = "Date"
	p.Y.Label.Text = "Price"

	// Format X-axis to show dates
	p.X.Tick.Marker = plot.TimeTicks{Format: "2006-01-02"}

	// Plot raw price data
	line, err := plotter.NewLine(pts)
	if err != nil {
		return fmt.Errorf("error creating line plot for %s: %v", symbol, err)
	}
	line.Color = color.RGBA{B: 255, A: 255} // Blue for raw price
	p.Add(line)

	// Calculate and plot 50-day SMA
	if len(rawPrices) >= 50 {
		sma50 := calculateSMA(rawPrices, 50)
		sma50Pts := make(plotter.XYs, len(sma50))
		for i := range sma50 {
			sma50Pts[i].X = float64(timestamps[i].Unix())
			sma50Pts[i].Y = sma50[i]
		}
		line50, err := plotter.NewLine(sma50Pts)
		if err != nil {
			return fmt.Errorf("error creating 50-day SMA line plot for %s: %v", symbol, err)
		}
		line50.Color = color.RGBA{G: 255, A: 255} // Green for 50-day SMA
		p.Add(line50)
		p.Legend.Add("50-day SMA", line50)
	} else {
		log.Printf("Not enough data for 50-day SMA for %s", symbol)
	}


	// Calculate and plot 200-day SMA
	if len(rawPrices) >= 200 {
		sma200 := calculateSMA(rawPrices, 200)
		sma200Pts := make(plotter.XYs, len(sma200))
		for i := range sma200 {
			sma200Pts[i].X = float64(timestamps[i].Unix())
			sma200Pts[i].Y = sma200[i]
		}
		line200, err := plotter.NewLine(sma200Pts)
		if err != nil {
			return fmt.Errorf("error creating 200-day SMA line plot for %s: %v", symbol, err)
		}
		line200.Color = color.RGBA{R: 255, A: 255} // Red for 200-day SMA
		p.Add(line200)
		p.Legend.Add("200-day SMA", line200)
	} else {
		log.Printf("Not enough data for 200-day SMA for %s", symbol)
	}

	p.Legend.Add("Price", line) // Add price legend last to be on top

	// Save the plot to a PNG file
	if err := p.Save(8*vg.Inch, 6*vg.Inch, filename); err != nil { // Increased size for better visibility
		return fmt.Errorf("error saving plot for %s: %v", symbol, err)
	}

	log.Printf("Generated chart for %s: %s", symbol, filename)
	return nil
}