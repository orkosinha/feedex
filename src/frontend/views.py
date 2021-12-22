from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from fetcher.models import Provider
from fetcher.fetch import fetch_and_preview
from frontend.retriever import build_feed
from fetcher.scraper import get_favicon
from frontend.forms import AddFeedForm


def index(request):
    context = {
        "segment": "index",
        "feed": build_feed(),
        "providers": Provider.objects.all(),
    }

    html_template = loader.get_template("home/index.html")
    return HttpResponse(html_template.render(context, request))


def pages(request):
    context = {"providers": Provider.objects.all()}

    try:
        # Embed a fresh feed if requested
        slug = request.GET.get("slug", None)
        if slug:
            provider = Provider.objects.get(slug=slug)
            context["feed"] = {provider.name: fetch_and_preview(slug)}
            context["description"] = provider.description

        # All resource paths end in .html.
        # Pick out the html file name from the url. And load that template.
        load_template = request.path.split("/")[-1]

        if load_template == "admin":
            return HttpResponseRedirect(reverse("admin:index"))
        elif load_template == "add-feed.html":
            if request.method == "POST":
                form = AddFeedForm(request.POST)

                if form.is_valid():
                    provider = Provider(
                        slug=form.cleaned_data["slug"],
                        name=form.cleaned_data["name"],
                        provider_type="rss",
                        feed_url=form.cleaned_data["feed_url"],
                        base_url=form.cleaned_data["base_url"],
                        icon=get_favicon(form.cleaned_data["base_url"]),
                        description=form.cleaned_data["description"],
                    )
                    provider.save()

            else:
                form = AddFeedForm()
                context["form"] = form

        context["segment"] = load_template

        html_template = loader.get_template("home/" + load_template)

        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template("home/page-404.html")
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template("home/page-500.html")
        return HttpResponse(html_template.render(context, request))
