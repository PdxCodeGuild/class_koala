from django.shortcuts import render
from .models import URL
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404, render

import random, string



def index(request):

    long_urls = URL.objects.order_by('-pub_date')[:5]
    context = {'long_urls': long_urls}
    return render(request, 'short/index.html', context)

def coder(request):
    short_code = ""
    letter_choices= ['b', 'c', 'd', 'e', 'f']
    choices = (string.ascii_lowercase + string.punctuation)
    short_code = short_code + (random.choice (choices)+ (random.choice (letter_choices)))
    context = {'short_code': short_code}

    return render(request, 'short/index.html', context)