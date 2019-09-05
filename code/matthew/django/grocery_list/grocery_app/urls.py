from django.urls import path
from . import views

app_name = 'grocery_app'
urlpatterns = [
    path('', views.index, name='index'), # /grocery_app/
    path('additem/', views.additem, name='additem'), # /grocery_app/additem/
    path('completeditem/<int:pk>', views.completeditem, name='completeditem') #/grocery_app/completeditem
]