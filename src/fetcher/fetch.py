from datetime import datetime
from dateutil import parser as date_parser
from django.db import transaction
from fetcher.models import Provider, Content
import feedparser
import json

STATES_LOCATION = "./states"


def parse_date(date):
    if date:
        return date_parser.parse(date)
    return datetime.today()


def fetch_and_preview(provider_slug):
    provider = Provider.objects.get(slug=provider_slug)
    entries = fetch(provider, ignore_predicates=True)

    return [
        Content(
            provider=provider,
            title=e.title,
            date=parse_date(e.published),
            url=e.link,
            description="",
        )
        for e in entries
    ]


def fetch_and_store():
    providers = Provider.objects.all()

    for p in providers:
        entries = fetch(p)
        # Parse and input into db
        for e in entries:
            entry, _ = Content.objects.update_or_create(
                url=e.link,
                defaults={
                    "provider": p,
                    "title": e.title,
                    "url": e.link,
                    "date": parse_date(e.published),
                    "description": "",
                },
            )


def fetch(provider, ignore_predicates=False):
    state_file = f"{STATES_LOCATION}/.state_{provider.slug}.json"

    # Get state files, if none exist initialize to empty
    if not ignore_predicates:
        try:
            with open(state_file, "r") as f:
                predicates = json.load(f)
        except:
            predicates = {}
    predicates = {}

    # Run parser with loaded predicates
    try:
        feed = feedparser.parse(
            provider.feed_url,
            **predicates,
        )
    except:
        return []

    # Check if resource has been read before
    if feed.status == 304:
        return []

    # Save new predicates
    wanted_predicate_keys = ["etag", "modified"]
    new_predicates = dict((k, feed[k]) for k in wanted_predicate_keys if k in feed)
    with open(state_file, "w") as f:
        json.dump(new_predicates, f)

    return feed.entries
