from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Post

class ChirpListView(ListView):
    model = Post
    template_name = 'home.html'

class ChirpDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class ChirpCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['post_text', 'author']

