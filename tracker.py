import requests
from bs4 import BeautifulSoup

def fetch_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        title = soup.find("span", class_="B_NuCI").text.strip()
        price = soup.find("div", class_="_30jeq3 _16Jk6d").text.strip()
        return title, float(price.replace("₹", "").replace(",", ""))
    except AttributeError:
        return "Product Not Found", None
