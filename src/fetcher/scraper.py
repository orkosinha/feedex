from bs4 import BeautifulSoup
import requests


def get_favicon(base_url):
    # TODO: Make this less hacky
    page = requests.get(base_url, headers={"User-Agent": "Mozilla/5.0"})
    if "cornell" in base_url:
        print(page.text)
    soup = BeautifulSoup(page.text, "html.parser")
    icon_link = soup.find("link", rel="shortcut icon")
    if icon_link is None:
        icon_link = soup.find("link", rel="icon")
    if icon_link is None:
        icon_link = soup.find("link", rel="apple-touch-icon")
    if icon_link is None:
        return base_url + "/favicon.ico"
    return icon_link["href"]
