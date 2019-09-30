from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
