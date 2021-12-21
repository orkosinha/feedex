import datetime
from django import forms
from django.core.exceptions import ValidationError


class AddFeedForm(forms.Form):
    slug = forms.SlugField(help_text="Enter a unique name for this provider")
    name = forms.CharField(help_text="Enter a name for this provider")
    feed_url = forms.URLField(help_text="Enter the feed url")
    base_url = forms.URLField(help_text="Enter the home page for this provider")
    description = forms.CharField(help_text="Enter a description for this provider")
