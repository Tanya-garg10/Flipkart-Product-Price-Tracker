from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
import time
from email_utils import send_email

def fetch_price():
    # Load config.json
    with open("config.json", "r") as file:
        config = json.load(file)

    url = config["url"]
    target_price = config["target_price"]

    # Headless Chrome
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Start browser
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(3)  # wait for the page to load

    try:
        # Find the price element using Flipkart class name
        price_element = driver.find_element(By.CLASS_NAME, "_30jeq3._16Jk6d")
        price_text = price_element.text.strip().replace("₹", "").replace(",", "")
        current_price = int(price_text)

        print(f"✅ Current Price: ₹{current_price}")

        if current_price <= target_price:
            subject = "🔔 Flipkart Price Alert"
            message = f"The price dropped to ₹{current_price}!\nCheck it here: {url}"
            send_email(subject, message)
            print("📧 Email alert sent!")

        return current_price

    except NoSuchElementException:
        print("❌ Could not fetch the product price.")
        return None
    finally:
        driver.quit()

# Uncomment to test standalone
# if __name__ == "__main__":
#     fetch_price()
