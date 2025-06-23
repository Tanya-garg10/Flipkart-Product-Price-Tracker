import streamlit as st
import json
from selenium_tracker import fetch_price

# Load configuration from config.json
try:
    with open("config.json", "r") as f:
        config = json.load(f)
    product_url = config["url"]
    target_price = config["target_price"]
except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
    st.error("❌ Error loading config.json. Please check the file format.")
    st.stop()

# Streamlit Page Settings
st.set_page_config(page_title="Flipkart Price Tracker", page_icon="📦")
st.title("📦 Flipkart Product Price Tracker")

# Display product URL and target
st.markdown(f"🔗 **Product URL:** [Click here to view product]({product_url})", unsafe_allow_html=True)
st.markdown(f"🎯 **Target Price:** ₹{target_price}")

# Track current price using Selenium
with st.spinner("Checking current price on Flipkart..."):
    current_price, _ = fetch_price()

# Handle result
if current_price:
    st.success(f"✅ Current Price: ₹{current_price}")
    
    if current_price <= target_price:
        st.balloons()
        st.warning("🎉 Good news! The price dropped below your target. Check your email for the alert.")
    else:
        st.info("ℹ️ Still above your target price. Try again later.")
else:
    st.error("❌ Could not fetch the current price. Please check the product URL or selector.")

