from django.db import models


class Provider(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    feed_url = models.URLField(max_length=200)
    base_url = models.URLField(max_length=200)
    icon = models.URLField(max_length=500)
    description = models.CharField(max_length=500)


class Content(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField()
    url = models.URLField(max_length=200, unique=True)
    description = models.CharField(max_length=500)
