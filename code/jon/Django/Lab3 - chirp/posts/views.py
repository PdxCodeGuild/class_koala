from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Posts

class PostsListView(ListView):
    model = Posts
    template_name = 'home.html'

    def get_queryset(self):
        return Posts.objects.order_by('-created')

class PostsDetailView(DetailView):
    model = Posts
    template_name = "post_detail.html"

class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    template_name: "post_new.html"
    fields = ["body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)