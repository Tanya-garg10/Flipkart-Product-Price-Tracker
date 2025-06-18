import streamlit as st
import json
from tracker import fetch_price

st.title("📦 Flipkart Product Price Tracker")

with open("config.json") as f:
    config = json.load(f)

url = config["product_url"]
target = config["desired_price"]

st.write(f"🔗 [View Product]({url})")

title, price = fetch_price(url)

if price:
    st.subheader(f"{title}")
    st.metric("Current Price", f"₹{price}")
    if price <= target:
        st.success("🎯 Price dropped below target!")
    else:
        st.warning("🔔 Not yet at target price.")
else:
    st.error("❌ Could not fetch the product price.")
