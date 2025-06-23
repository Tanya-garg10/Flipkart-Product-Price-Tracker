from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

def fetch_price():
    try:
        # Load config
        with open("config.json", "r") as f:
            config = json.load(f)
        url = config["url"]

        # Setup headless Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.get(url)
        time.sleep(5)  # Let the page load

        # ✅ Get product title
        title_elem = driver.find_element(By.CLASS_NAME, "_2KFngB")
        title = title_elem.text.strip()

        # ✅ Get product price (₹ symbol is usually included)
        price_elem = driver.find_element(By.CLASS_NAME, "_30jeq3")
        price_text = price_elem.text.strip().replace("₹", "").replace(",", "")
        price = float(price_text)

        driver.quit()
        return price, title

    except Exception as e:
        print("❌ Error in fetch_price():", e)
        return None, None

