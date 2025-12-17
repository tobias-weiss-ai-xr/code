package main

import (
		"fmt"
		"log"
	
	
		"stock-market-retriever/database"
		"stock-market-retriever/data_generator"
		"stock-market-retriever/performance"
		"stock-market-retriever/charts" // Import the new charts package
	)



func main() {
	// List of German stock symbols to fetch (DAX components)
	symbols := []string{
		"ADS.DE", "ALV.DE", "BAS.DE", "BAYN.DE", "BEI.DE", "BMW.DE", "CON.DE", "1COV.DE", "DAI.DE",
		"DHER.DE", "DBK.DE", "DB1.DE", "DPW.DE", "DTE.DE", "DWNI.DE", "EOAN.DE", "FRE.DE",
		"FME.DE", "HEI.DE", "HEN3.DE", "IFX.DE", "LIN.DE", "MRK.DE", "MTX.DE", "MUV2.DE",
		"RWE.DE", "SAP.DE", "SIE.DE", "VOW3.DE", "VNA.DE",
	}

	// Fetch stock data
	stocks, err := data_generator.FetchStockData(symbols)
	if err != nil {
		log.Fatalf("Error fetching stock data: %v", err)
	}

	// Connect to the database
	db, err := database.ConnectToDB()
	if err != nil {
		log.Fatalf("Error connecting to database: %v", err)
	}
	defer db.Close()

	// Create the table if it doesn't exist
	if err := database.CreateTable(db); err != nil {
		log.Fatalf("Error creating table: %v", err)
	}

	// Save the stock data to the database
	if err := database.SaveStockData(db, stocks); err != nil {
		log.Fatalf("Error saving stock data: %v", err)
	}

	fmt.Println("Successfully fetched and saved stock data.")

	// Calculate and display stock performance
	nMonths := 24 // Example: 2-year performance
	stockPerformance, err := performance.GetStockPerformance(db, symbols, nMonths)
	if err != nil {
		log.Fatalf("Error calculating stock performance: %v", err)
	}

	fmt.Println("\nStock Performance:")
	for symbol, perfData := range stockPerformance {
		fmt.Printf("  %s:\n", symbol)
		for period, value := range perfData {
			fmt.Printf("    %s: %.2f%%\n", period, value)
		}
	}

	fmt.Println("\nGenerating stock price charts in 'gfx/' folder...")
	for _, symbol := range symbols {
		filename := fmt.Sprintf("gfx/%s.png", symbol)
		if err := charts.GenerateStockPriceChart(db, symbol, filename); err != nil {
			log.Printf("Error generating chart for %s: %v", symbol, err)
		}
	}
	fmt.Println("Finished generating stock price charts.")
}






