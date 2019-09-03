from django.urls import path
from . import views

app_name = "url_app"
urlpatterns = [
    path("", views.index, name="index"), # /url_app/
    path("submit/", views.submit, name="submit"), # /url_app/submit/
    path("redirect/", views.redirect, name="redirect"), # url_app/redirect/
]

