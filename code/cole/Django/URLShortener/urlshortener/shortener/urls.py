from django.urls import path

from . import views

app_name = 'URLShortener'

urlpatterns = [
    path('', views.index.as_view(), name = 'index'),
    path('new', views.new.as_view(), name = 'new'),
    path('createShortURL/<int:pk>', views.createShortURL, name = 'createShortURL'),
    path('redirect/<str:urlcode>', views.redirect, name = 'redirect')
]
