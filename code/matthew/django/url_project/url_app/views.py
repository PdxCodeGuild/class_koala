import random
import string

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import UrlShortener

def codeGenerator(stringLength=6):
    """
    generates a random six character code comprised of lowercase and uppercase letters, as well as digits.
    """
    code = string.ascii_letters + string.digits
    return "".join(random.choice(code) for i in range(stringLength))

def index(request):
    url_list = UrlShortener.objects.all()
    context = {"url_list": url_list}
    return render(request, "url_app/index.html", context)

def submit(request):
    code = codeGenerator()
    UrlShortener.objects.create(code = code, long_url = request.POST["long_url"])
    return HttpResponseRedirect(reverse("url_app:index"))

def redirect(request):
    short_url = request.POST["short_url"]
    selected_url = UrlShortener.objects.get(code=short_url)
    redirected_url = selected_url.long_url
    return HttpResponseRedirect(redirected_url)