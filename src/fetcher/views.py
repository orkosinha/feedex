from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from fetcher.models import Provider


class ProviderPage(TemplateView):
    def get(self, request, **kwargs):
        print(Provider.objects.all())
        return render(
            request,
            "index.html",
            {
                "providers": Provider.objects.all(),
            },
        )
