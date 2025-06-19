import requests
from bs4 import BeautifulSoup

def fetch_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        # Title
        title = soup.find("span", class_="B_NuCI").get_text(strip=True)

        # Price
        price_div = soup.find("div", class_="_30jeq3 _16Jk6d")
        if not price_div:
            print("❌ Price tag not found.")
            return None, None

        price_text = price_div.get_text(strip=True).replace("₹", "").replace(",", "")
        price = float(price_text)

        return title, price

    except Exception as e:
        print("❌ Could not fetch the product price.")
        print("⚠️ Error:", e)
        return None, None

