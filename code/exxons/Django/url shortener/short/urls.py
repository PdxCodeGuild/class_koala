from django.urls import path
from . import views

app_name = 'short'
urlpatterns = [
    path('short/', views.index, name='index')
]