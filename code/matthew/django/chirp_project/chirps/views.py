from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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

class ChirpCreateView(CreateView):
    model = Chirp
    template_name = "chirps/chirp_new.html"
    fields = ["body"]

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)