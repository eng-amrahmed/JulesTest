import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Stock Information App")

st.title("Stock Information App")

ticker_symbol = st.text_input("Enter Stock Ticker", "").upper()

if ticker_symbol:
    try:
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info

        current_price = info.get('currentPrice') or info.get('regularMarketPrice')
        pe_ratio = info.get('trailingPE') or info.get('forwardPE')

        if current_price is not None:
            st.metric(label=f"{ticker_symbol} Current Price", value=f"${current_price:.2f}")
        else:
            st.error(f"Price data not available for {ticker_symbol}.")

        if pe_ratio is not None:
            st.metric(label=f"{ticker_symbol} P/E Ratio", value=f"{pe_ratio:.2f}")
        else:
            st.error(f"P/E ratio data not available for {ticker_symbol}.")

    except Exception as e:
        st.error(f"Error fetching data for {ticker_symbol}: Invalid ticker or data not available.")
        st.error(f"Details: {e}")

else:
    st.info("Please enter a stock ticker symbol to see its information.")
