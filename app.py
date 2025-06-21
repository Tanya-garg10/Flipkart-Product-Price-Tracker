import streamlit as st
import json
from selenium_tracker import fetch_price
from notifier import send_email  # Optional: Only if email alert is used

# Load config
with open("config.json") as f:
    config = json.load(f)

url = config["product_url"]
target_price = config["desired_price"]

st.title("📦 Flipkart Price Tracker")
st.markdown(f"[🔗 View Product]({url})", unsafe_allow_html=True)

title, price = fetch_price(url)

if not title or not price:
    st.error("❌ Could not fetch the product price.")
else:
    st.subheader(title)
    st.write(f"💰 Current Price: ₹{price}")
    st.write(f"🎯 Target Price: ₹{target_price}")

    if price <= target_price:
        st.success("✅ Great! The price is within your budget!")
        # send_email(title, price)  # Optional: enable if email is needed
    else:
        st.warning("⏳ Price is still above your target.")
