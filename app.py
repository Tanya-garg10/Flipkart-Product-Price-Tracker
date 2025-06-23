import streamlit as st
import json
from selenium_tracker import fetch_price

# Load config
with open("config.json") as f:
    config = json.load(f)

product_url = config["url"]
target_price = config["target_price"]

st.set_page_config(page_title="Flipkart Product Price Tracker", page_icon="📦")

st.title("📦 Flipkart Product Price Tracker")
st.markdown("Track your product prices in real-time and get alerts when they drop! 🎯")

st.markdown(f"🔗 [View Product]({product_url})")

title, price = fetch_price(product_url)

if price is not None:
    st.success(f"**{title}**\n\n💰 Current Price: ₹{price}")

    if price <= target_price:
        st.balloons()
        st.warning("🎉 Good news! Price dropped below your target.")
else:
    st.error("❌ Could not fetch the product price.")

