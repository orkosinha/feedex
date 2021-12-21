from django.apps import AppConfig
import sys


class FetcherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fetcher"

    def ready(self):
        from fetcher import scheduler

        if "runserver" in sys.argv:
            scheduler.start()
