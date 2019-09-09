from django.urls import path

from . import views

app_name = 'GroceryList'

urlpatterns = [
    path('', views.itemList.as_view(), name = 'list'),
    path('addItem', views.addItem.as_view(), name = 'add'),
    path('complete/<int:pk>', views.complete, name = 'complete'),
    path('uncomplete/<int:pk>', views.uncomplete, name = 'uncomplete'),
]
