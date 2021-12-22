import requests
from fetcher.models import Content
from fetcher.connectors.common import parse_date

ISSUU_BASE = "https://issuu.com/call/profile/v1/documents/"


def fetch_issuu(provider):
    res = requests.get(ISSUU_BASE + provider.slug).json()
    return [
        Content(
            provider=provider,
            title=item["title"],
            url=f"https://issuu.com/{provider.slug}/docs/{item['uri']}?ff",
            date=parse_date(item["publishDate"]),
            description="",
        )
        for item in res["items"]
    ]
