import random
import string

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import UrlShortener, ClickData

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
    """
    accepts full length of URL, stores it in database with randomly generated six digit custom code, then displays it back to user
    """
    code = codeGenerator()
    UrlShortener.objects.create(code = code, long_url = request.POST["long_url"])
    code_message = f"New Code: {code} - Please keep for records. To use in browser, add code/{code} to existing URL."
    messages.success(request, code_message)
    return HttpResponseRedirect(reverse("url_app:index"))

def redirect(request, short_url):
    """
    accepts a six character shortened URL, checks if it exists in database and redirects user to full length URL, if so; also, adds user instance to database and increases # of clicks on respective URL
    """
    selected_url = UrlShortener.objects.get(code = short_url)
    redirected_url = selected_url.long_url
    ip = request.META['REMOTE_ADDR']
    ClickData.objects.create(ip = ip, url_code = short_url)
    selected_url.clicks += 1
    selected_url.save()
    return HttpResponseRedirect(redirected_url)