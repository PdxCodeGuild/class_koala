from django.urls import path
from . import views

app_name = 'groceryList'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('completed/<int:pk>', views.completed, name='completed'),
    path('delete', views.delete, name='delete'),
]
