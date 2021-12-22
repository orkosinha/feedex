import feedparser
import json
from fetcher.models import Content
from fetcher.connectors.common import parse_date

STATES_LOCATION = "./states"


def fetch_rss(provider, ignore_predicates=True):
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

    return [
        Content(
            provider=provider,
            title=e.title,
            url=e.link,
            date=parse_date(e.published),
            description="",
        )
        for e in feed.entries
    ]
