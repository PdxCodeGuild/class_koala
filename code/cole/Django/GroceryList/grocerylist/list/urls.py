from django.urls import path

from . import views

app_name = 'GroceryList'

urlpatterns = [
    path('', views.new_item, name = 'new_item')
]
