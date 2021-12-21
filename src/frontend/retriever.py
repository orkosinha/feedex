from fetcher.models import Provider, Content


def by_provider(provider_slug, limit=5):
    content = Content.objects.filter(provider=provider_slug)
    return content[:limit]


def build_feed():
    feed = {}
    for p in Provider.objects.all():
        feed[p] = by_provider(p.slug)
    return feed
