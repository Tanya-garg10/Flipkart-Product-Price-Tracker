import streamlit as st
import json
from selenium_tracker import fetch_price

# Load configuration
try:
    with open("config.json", "r") as f:
        config = json.load(f)
    product_url = config["url"]
    target_price = config["target_price"]
except Exception as e:
    st.error(f"❌ Error loading config.json: {e}")
    st.stop()

# Streamlit app UI
st.set_page_config(page_title="Flipkart Price Tracker", page_icon="📦")
st.title("📦 Flipkart Product Price Tracker")
st.markdown(f"🔗 **Product URL:** [View Product]({product_url})", unsafe_allow_html=True)
st.markdown(f"🎯 **Target Price:** ₹{target_price}")

# Fetch current price
with st.spinner("Fetching price from Flipkart..."):
    current_price, product_title = fetch_price()

# Display results
if current_price:
    st.success(f"✅ **{product_title}** is now ₹{current_price}")

    if current_price <= target_price:
        st.balloons()
        st.warning("🎉 Good news! Price has dropped below your target.")

