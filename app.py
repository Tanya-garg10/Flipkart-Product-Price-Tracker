import streamlit as st
import json
from selenium_tracker import fetch_price
from email_utils import send_email  # Optional email module

# Load configuration
try:
    with open("config.json") as f:
        config = json.load(f)
    product_url = config["url"]
    target_price = config["target_price"]
except Exception as e:
    st.error("❌ Error loading config.json. Please check the file format.")
    st.stop()

st.title("📦 Flipkart Product Price Tracker")
st.markdown(f"🔗 **Product URL:** [View Product]({product_url})")
st.markdown(f"🎯 **Target Price:** ₹{target_price}")

current_price, _ = fetch_price()

if current_price:
    st.success(f"✅ Current Price: ₹{current_price}")
    if current_price <= target_price:
        st.balloons()
        st.markdown("🎉 **Good news! The price dropped below your target. Check your email for the alert.**")
        send_email(current_price)  # Only if email alerts are configured
    else:
        st.info("🔍 Still waiting for price to drop...")
else:
    st.error("❌ Could not fetch the product price.")

    with open("config.json", "r") as f