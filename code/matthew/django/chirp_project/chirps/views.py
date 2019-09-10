from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Chirp

class ChirpListView(ListView):
    template_name = "chirps/home.html"

    def get_queryset(self):
        return Chirp.objects.order_by("-created")

class ChirpDetailView(DetailView):
    model = Chirp
    template_name = "chirps/chirp_detail.html"

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Chirp
    template_name = "chirps/chirp_new.html"
    fields = ["body"]
    success_url = reverse_lazy("chirps:home")

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
    
class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chirp
    template_name = "chirps/chirp_delete.html"
    success_url = reverse_lazy("chirps:home")

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.username