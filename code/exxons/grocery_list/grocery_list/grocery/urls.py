from django.urls import path 
from . import views 

app_name = 'grocery'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.items, name='item'),
    path('deleted/<int:pk>', views.delete_item, name='delete_item'),
    path('completed/<int:pk>', views.complete_items, name='complete_items')
]

