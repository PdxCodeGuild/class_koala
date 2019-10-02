from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import chirp
# Create your views here.


class HomeView(ListView):
    model = chirp
    template_name = 'home.html'

    def get_queryset(self):
        return chirp.objects.order_by("-postDate")

class NewChirpView(LoginRequiredMixin, CreateView):
    model = chirp
    template_name = 'newChirp.html'
    fields = ['chirpText']
    success_url = reverse_lazy("chirps:home")

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class ChirpDetailView(DetailView):
    model = chirp
    template_name = 'detail.html'

class DeleteChirpView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = chirp
    template_name = 'delete.html'
    success_url = reverse_lazy("chirps:home")

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.username
