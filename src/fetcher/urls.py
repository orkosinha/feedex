from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProviderPage.as_view()),
]
