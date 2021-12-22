from bs4 import BeautifulSoup
import requests


def get_favicon(base_url):
    # TODO: Make this less hacky
    page = requests.get(base_url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(page.text, "html.parser")
    icon_link = soup.find("link", rel="shortcut icon")
    if icon_link is None:
        icon_link = soup.find("link", rel="icon")
    if icon_link is None:
        icon_link = soup.find("link", rel="apple-touch-icon")
    if icon_link is None or icon_link["href"][0] == "/":
        return "https://issuu.com/favicon.ico"
    return icon_link["href"]
