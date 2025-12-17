package main

import (
	"testing"
	"strings"
)

func TestFetchStockData_DummyDataGeneration(t *testing.T) {
	symbols := []string{"TEST_SYMBOL_1", "TEST_SYMBOL_2"}
	stocks, err := fetchStockData(symbols)

	if err != nil {
		t.Fatalf("fetchStockData returned an unexpected error: %v", err)
	}

	if len(stocks) != len(symbols) {
		t.Errorf("Expected %d stocks, but got %d", len(symbols), len(stocks))
	}

	for _, stock := range stocks {
		if !strings.HasPrefix(stock.Name, "Dummy Name for") {
			t.Errorf("Expected dummy name, but got %s for symbol %s", stock.Name, stock.Symbol)
		}
		// Further assertions can be added to check other dummy data properties
	}
}