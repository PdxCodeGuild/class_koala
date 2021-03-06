import random
import string

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import StartingURL
from django.contrib import messages

def index(request):
    long_url = StartingURL.objects.all()
    short_code = StartingURL.objects.all()
    context = {'long_url': long_url, 'short_code':short_code}
    return render(request, 'shortenerApp/index.html', context)

def add(request):

    def randomStringDigits(stringLength=6):
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range (stringLength))

    shortcode = randomStringDigits()
    StartingURL.objects.create(longurl = request.POST['longurl'], code = shortcode)

    code_message = f"Your new short URL is ready!  You can now use http://localhost:8000/{shortcode}"

    messages.success(request, code_message)

    return HttpResponseRedirect(reverse('shortenerApp:index'))

def urlredirect(request, code):
    shortcode = get_object_or_404(StartingURL, code = code)

    longUrl = shortcode.longurl

    return HttpResponseRedirect(longUrl)







