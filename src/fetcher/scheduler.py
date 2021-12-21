from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from fetcher.fetch import fetch_and_store
from fetcher.models import Provider
from fetcher.scraper import get_favicon
import json
from pathlib import Path
import shutil
import os

STATES_PATH = Path("./states")


def start():
    with open("providers.json") as f:
        providers = json.load(f)
        for p in providers:
            if not Provider.objects.filter(
                slug=p, feed_url=providers[p]["feed_url"]
            ).exists():
                provider = Provider(
                    slug=p,
                    name=providers[p]["name"],
                    feed_url=providers[p]["feed_url"],
                    base_url=providers[p]["base_url"],
                    icon=get_favicon(providers[p]["base_url"]),
                    description=providers[p]["description"],
                )
                provider.save()

    # Before first run, clear states
    if STATES_PATH.exists():
        shutil.rmtree(STATES_PATH)
    STATES_PATH.mkdir()
        

    fetch_and_store()
    scheduler = BackgroundScheduler(timezone="US/Eastern")
    scheduler.add_job(fetch_and_store, "interval", seconds=300, max_instances=1)
    scheduler.start()
