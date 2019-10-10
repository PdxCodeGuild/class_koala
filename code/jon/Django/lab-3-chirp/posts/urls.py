from django.urls import path

from .views import ChirpListView, ChirpDetailView, ChirpCreateView

urlpatterns = [
    path('', ChirpListView.as_view(), name='home'),
    path('post/<int:pk>', ChirpDetailView.as_view(), name='post_detail'),
    path('post/new/', ChirpCreateView.as_view(), name='post_new'),

]
