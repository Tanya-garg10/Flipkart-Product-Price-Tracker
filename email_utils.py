import smtplib
from email.mime.text import MIMEText
import os
import json

def send_email(current_price):
    with open("config.json") as f:
        config = json.load(f)

    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receiver = config.get("receiver_email", sender)

    msg = MIMEText(f"The current price is ₹{current_price}. It's below your target price!")
    msg['Subject'] = "🔔 Price Drop Alert!"
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

