# German Stock Market Retriever

This program fetches the latest stock market data for German stocks (DAX components) and saves it to a MySQL database.

## Prerequisites

- Docker
- Docker Compose

## Running with Docker Compose

This is the recommended way to run the application.

1. **Clone the repository or download the source code.**
2. **Set up the environment variables:**
   Create a `.env` file in the root of the project and add the following content:
   ```
   MYSQL_ROOT_PASSWORD=mysecretpassword
   MYSQL_DATABASE=stock_db
   MYSQL_USER=user
   MYSQL_PASSWORD=password
   ```
   You can change the values to your liking.
3. **Run the application:**
   ```bash
   docker-compose up --build
   ```

The application will be built and started, along with a MySQL database. The application will then:
- Fetch the latest stock data for the predefined list of German stocks.
- Connect to the MySQL database.
- Create a `stocks` table if it doesn't already exist.
- Save the fetched stock data into the `stocks` table.

### Known Issues and Limitations

- **Stock Data Retrieval (piquette/finance-go library):** The application currently uses the `piquette/finance-go` library to fetch stock data from Yahoo Finance. Extensive testing has revealed that this library is currently unable to reliably retrieve *any* real stock data, consistently returning "Can't find quote for symbol". This means the application, as is, cannot fetch live stock data.
  - To enable live data fetching, a replacement for the `piquette/finance-go` library is required.
  - The application is currently configured to use dummy data for demonstration purposes, ensuring the database integration and overall pipeline functionality can still be tested.

## Development

### Prerequisites

- Go (version 1.18 or later)
- A running MySQL server

### Setup

1. **Install the dependencies:**
   ```bash
   go get
   ```
2. **Configure the database connection:**
   The application is configured to read database credentials from environment variables. You can set them in your shell:
   ```bash
   export DB_USER=your_username
   export DB_PASS=your_password
   export DB_NAME=your_database
   export DB_HOST=localhost
   ```
3. **Create the database:**
   Ensure that the database specified in `DB_NAME` exists in your MySQL server.

### Usage

Run the program from the command line:

```bash
go run main.go
```
