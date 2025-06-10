# Stock Information App

This is a simple web application built with Python and Streamlit that fetches and displays the current stock price and P/E ratio for a given stock ticker using the Yahoo Finance API (`yfinance`).

## Features

-   Enter a stock ticker symbol (e.g., AAPL, GOOGL, MSFT).
-   View the current stock price.
-   View the stock's P/E (Price-to-Earnings) ratio.
-   Error messages for invalid tickers or when data is not available.

## Setup and Usage

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    -   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    This will typically open the application in your default web browser.

## Dependencies

-   [Streamlit](https://streamlit.io/): For creating the web interface.
-   [yfinance](https://pypi.org/project/yfinance/): For fetching stock data from Yahoo Finance.

Replace `<repository_url>` and `<repository_directory>` with the actual URL and directory name if applicable when cloning.
