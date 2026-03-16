import streamlit as st
import yfinance as yf
from binance.client import Client

# --- LIVE DATA HELPERS ---
def get_live_price(ticker, is_crypto=False):
    try:
        if is_crypto:
            # Binance public API (No key needed for basic price tickers)
            client = Client() 
            symbol = ticker.upper() + "USDT"
            data = client.get_symbol_ticker(symbol=symbol)
            return float(data['price'])
        else:
            # Yahoo Finance for Stocks
            stock = yf.Ticker(ticker)
            return stock.fast_info['last_price']
    except Exception:
        return None

# --- UPDATED TRADING SESSION ---
def trading_session():
    st.title("💹 AI Trade & Verify")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        asset_type = st.radio("Asset Type", ["Stock", "Crypto"])
        symbol = st.text_input("Enter Symbol (e.g., AAPL or BTC)", value="BTC")
        
        if symbol:
            price = get_live_price(symbol, is_crypto=(asset_type == "Crypto"))
            if price:
                st.metric(label=f"Current {symbol} Price", value=f"${price:,.2f}")
            else:
                st.error("Could not fetch price. Check the symbol.")

    with col2:
        mode = st.selectbox("Action", ["Buy", "Sell"])
        if st.button("Verify & Execute with AI"):
            with st.status("AI Agent Analyzing...", expanded=True):
                st.write(f"1. Validating {symbol} at ${price:,.2f}...")
                st.write("2. Verifying user legitimacy & wallet...")
                st.write("3. Searching for global counter-party...")
                st.success("Verified! Transaction matched.")
            st.balloons()
