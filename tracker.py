import requests
from bs4 import BeautifulSoup

def fetch_price(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Book title
        title = soup.find("h1").text.strip()

        # Price is in <p class="price_color">£51.77</p>
        price_text = soup.find("p", class_="price_color").text.strip()
        price = float(price_text.replace("£", ""))

        return title, price
    except Exception as e:
        print("Error fetching data:", e)
        return None, None
