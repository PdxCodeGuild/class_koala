from django.urls import path, include

from . import views

app_name = 'shortenerApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<str:code>/', views.urlredirect, name='redirect'),
    
]
