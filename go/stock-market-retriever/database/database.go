package database

import (
	"database/sql"
	"fmt"
	"os"

	_ "github.com/go-sql-driver/mysql"
	"stock-market-retriever/data_generator" // Import data_generator package
)

var (
	dbUser = os.Getenv("DB_USER")
	dbPass = os.Getenv("DB_PASS")
	dbName = os.Getenv("DB_NAME")
	dbHost = os.Getenv("DB_HOST")
)

// connectToDB connects to the MySQL database.
func ConnectToDB() (*sql.DB, error) {
	dsn := fmt.Sprintf("%s:%s@tcp(%s:3306)/%s", dbUser, dbPass, dbHost, dbName)
	db, err := sql.Open("mysql", dsn)
	if err != nil {
		return nil, err
	}
	if err := db.Ping(); err != nil {
		return nil, err
	}
	return db, nil
}

// createTable creates the stocks table if it doesn't exist.
func CreateTable(db *sql.DB) error {
	query := `
	CREATE TABLE IF NOT EXISTS stocks (
		id INT AUTO_INCREMENT PRIMARY KEY,
		symbol VARCHAR(20) NOT NULL,
		name VARCHAR(255) NOT NULL,
		price DECIMAL(10, 2),
		change_val DECIMAL(10, 2),
		change_percent DECIMAL(10, 4),
		day_high DECIMAL(10, 2),
		day_low DECIMAL(10, 2),
		year_high DECIMAL(10, 2),
		year_low DECIMAL(10, 2),
		volume BIGINT,
		fifty_two_week_high DECIMAL(10, 2),
		fifty_two_week_low DECIMAL(10, 2),
		timestamp DATETIME
	);`
	_, err := db.Exec(query)
	return err
}

// saveStockData saves the stock data to the database.
func SaveStockData(db *sql.DB, stocks []data_generator.Stock) error { // Use data_generator.Stock
	tx, err := db.Begin()
	if err != nil {
		return err
	}
	defer tx.Rollback()

	stmt, err := tx.Prepare(`
	INSERT INTO stocks (
		symbol, name, price, change_val, change_percent, day_high, day_low,
		year_high, year_low, volume, fifty_two_week_high,
		fifty_two_week_low, timestamp
	) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
	`)
	if err != nil {
		return err
	}
	defer stmt.Close()

	for _, stock := range stocks {
		_, err := stmt.Exec(
			stock.Symbol, stock.Name, stock.Price, stock.Change, stock.ChangePercent,
			stock.DayHigh, stock.DayLow, stock.YearHigh, stock.YearLow,
			stock.Volume, stock.FiftyTwoWeekHigh, stock.FiftyTwoWeekLow, stock.Timestamp,
		)
		if err != nil {
			return err
		}
	}

	return tx.Commit()
}