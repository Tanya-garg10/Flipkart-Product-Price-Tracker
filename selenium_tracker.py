# selenium_tracker.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def fetch_price(url):
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

        driver.get(url)
        time.sleep(5)  # Wait for page to load

        # Use updated selector based on Flipkart's structure
        price_element = driver.find_element(By.XPATH, "//div[contains(@class, '_30jeq3')]")
        price_text = price_element.text.strip().replace("₹", "").replace(",", "")
        driver.quit()

        return float(price_text)
    except Exception as e:
        print(f"[❌ ERROR] {e}")
        return None

