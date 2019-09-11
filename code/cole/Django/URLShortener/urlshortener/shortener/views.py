from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import URL

import random
# Create your views here.

class index(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return URL.objects.order_by('-createdTime')

class new(generic.CreateView):
    template_name = 'new.html'
    model = URL
    fields = ('longURL',)

def generateCode():
    string = ''
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    i = 0
    while i < 6:
        string += random.choice(chars)
        i+=1
    return string

def createShortURL(request, pk):
    url = get_object_or_404(URL, pk=pk)
    url.shortURL += "url.sh/"
    url.urlcode = generateCode()
    url.shortURL += url.urlcode
    url.save()
    return HttpResponseRedirect(reverse('URLShortener:index'))

def redirect(request, urlcode):
    url_list = URL.objects.order_by('-createdTime')
    for url in url_list:
        if urlcode == url.urlcode:
            return HttpResponseRedirect(url.longURL)
