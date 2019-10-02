from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration.html"
    success_url = reverse_lazy('login')

class UserProfileView(DetailView):
    model = User
    template_name = "profile.html"

    def get_object(self):
        return get_object_or_404(User, username = self.kwargs['username'])
