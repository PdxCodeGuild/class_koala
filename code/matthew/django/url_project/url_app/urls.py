from django.urls import path
from . import views

app_name = "url_app"
urlpatterns = [
    path("", views.index, name="index"), # /url_app/
    path("submit/", views.submit, name="submit"), # /url_app/submit/
    path("code/<short_url>", views.redirect, name="redirect"), # url_app/code/PMTJg9
    path("stats/<short_url>", views.stats, name="stats"), # url_app/stats/PMTJg9
]

