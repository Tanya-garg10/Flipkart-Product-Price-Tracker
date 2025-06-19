import streamlit as st
import json
from tracker import fetch_price

# Load config
with open("config.json") as f:
    config = json.load(f)

product_url = config["product_url"]
target_price = config["desired_price"]

st.title("📦 Flipkart Product Price Tracker")
st.markdown(f"[🔗 View Product]({product_url})", unsafe_allow_html=True)

title, current_price = fetch_price(product_url)

if title is None or current_price is None:
    st.error("❌ Could not fetch the product price. Try running locally.")
else:
    st.subheader(title)
    st.write(f"💰 Current Price: **£{current_price}**")
    st.write(f"🎯 Target Price: **£{target_price}**")

    if current_price <= target_price:
        st.success("✅ Great! The price is within your budget!")
    else:
        st.warning("⏳ Not yet. The price is still above your target.")
