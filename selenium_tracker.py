from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time

def fetch_price():
    try:
        with open("config.json") as f:
            config = json.load(f)

        url = config["url"]

        options = Options()
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options=options)
        driver.get(url)

        time.sleep(5)  # Wait for content to load

        try:
            price_element = driver.find_element(By.CLASS_NAME, "_30jeq3")
            price_text = price_element.text.strip().replace("₹", "").replace(",", "")
            price = int(price_text)
        except:
            price = None

        driver.quit()
        return price, url
    except Exception as e:
        print(f"❌ Error: {e}")
        return None, None


