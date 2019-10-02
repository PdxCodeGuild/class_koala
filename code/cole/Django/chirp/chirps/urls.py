from django.urls import path

from . import views

app_name = 'chirps'

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('chirp/new/', views.NewChirpView.as_view(), name = 'new'),
    path('chirp/<int:pk>/', views.ChirpDetailView.as_view(), name = 'detail'),
    path('chirp/<int:pk>/delete/', views.DeleteChirpView.as_view(), name='delete')
]
