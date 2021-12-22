from django.db import models


class Provider(models.Model):
    ISSUU = "ISU"
    RSS = "RSS"

    PROVIDER_TYPE_CHOICES = [(ISSUU, "issuu"), (RSS, "rss")]

    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    provider_type = models.CharField(
        max_length=3, choices=PROVIDER_TYPE_CHOICES, default="rss"
    )
    feed_url = models.URLField(max_length=200, default="")
    base_url = models.URLField(max_length=200)
    icon = models.URLField(max_length=500)
    description = models.CharField(max_length=500)


class Content(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField()
    url = models.URLField(max_length=200, unique=True)
    description = models.CharField(max_length=500)
