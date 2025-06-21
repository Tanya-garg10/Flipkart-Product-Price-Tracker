from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch_price(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    try:
        driver.get(url)
        time.sleep(5)

        title = driver.find_element(By.CLASS_NAME, "B_NuCI").text
        price_text = driver.find_element(By.CLASS_NAME, "_30jeq3").text
        price = float(price_text.replace("₹", "").replace(",", "").strip())

        return title, price
    except Exception as e:
        print("Error:", e)
        return None, None
    finally:
        driver.quit()
