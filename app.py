# app.py
import streamlit as st
import json
from selenium_tracker import fetch_price
import smtplib
from email.message import EmailMessage
import os

# Load config
try:
    with open("config.json", "r") as file:
        config = json.load(file)
    product_url = config["url"]
    target_price = float(config["target_price"])
except Exception as e:
    st.error(f"❌ Error loading config.json: {e}")
    st.stop()

# Streamlit UI
st.set_page_config(page_title="Flipkart Price Tracker", layout="centered")
st.title("📦 Flipkart Product Price Tracker")
st.markdown(f"🔗 **Product URL:** [View Product]({product_url})", unsafe_allow_html=True)
st.markdown(f"🎯 **Target Price:** ₹{target_price}")

# Fetch current price
current_price = fetch_price(product_url)
if current_price:
    st.success(f"✅ Current Price: ₹{current_price}")
    if current_price <= target_price:
        st.balloons()
        st.info("🎉 Price has dropped below your target!")
        # Send email alert
        sender = os.getenv("EMAIL_USER")
        password = os.getenv("EMAIL_PASS")
        recipient = os.getenv("EMAIL_TO")

        if sender and password and recipient:
            try:
                msg = EmailMessage()
                msg["Subject"] = "📉 Flipkart Price Drop Alert!"
                msg["From"] = sender
                msg["To"] = recipient
                msg.set_content(f"The product is now ₹{current_price}!\n\nCheck it here: {product_url}")

                with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                    smtp.starttls()
                    smtp.login(sender, password)
                    smtp.send_message(msg)
                st.success("📧 Email alert sent successfully!")
            except Exception as e:
                st.error(f"❌ Failed to send email: {e}")
else:
    st.error("❌ Could not fetch the product price.")
