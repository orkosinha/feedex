from django.db import transaction
from fetcher.models import Provider, Content
from fetcher.connectors.rss import fetch_rss
from fetcher.connectors.issuu import fetch_issuu


def fetch_and_preview(provider_slug):
    provider = Provider.objects.get(slug=provider_slug)
    return fetch(provider, ignore_predicates=True)


def fetch_and_store():
    providers = Provider.objects.all()

    for p in providers:
        content = fetch(p)

        # Parse and input into db
        for c in content:
            entry, _ = Content.objects.update_or_create(
                url=c.url,
                defaults={
                    "provider": c.provider,
                    "title": c.title,
                    "url": c.url,
                    "date": c.date,
                    "description": c.description,
                },
            )


def fetch(provider, ignore_predicates=False):
    if provider.provider_type == "rss":
        return fetch_rss(provider, ignore_predicates)
    elif provider.provider_type == "issuu":
        return fetch_issuu(provider)
    return []
