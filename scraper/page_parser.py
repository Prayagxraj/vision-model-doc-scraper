import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_model_page(url):

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("Failed:", url)
        return ""

    soup = BeautifulSoup(response.text, "html.parser")

    
    content = soup.find("article") or soup.find("main")

    if not content:
        return ""

    text = content.get_text(separator="\n", strip=True)

    if "Overview" in text:
        text = text.split("Overview", 1)[1]
        text = "Overview\n" + text

    return text