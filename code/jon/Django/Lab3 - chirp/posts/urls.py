from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostsListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostsDetailView.as_view(), name='detail'),
    path('post/new/', views.PostsCreateView.as_view(), name='newPost'),
]
