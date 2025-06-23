import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(os.getenv("EMAIL_ADDRESS"), os.getenv("TO_EMAIL"), email_message)
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

