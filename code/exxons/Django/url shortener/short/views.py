from django.shortcuts import render
from .models import URL
from django.urls  import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import get_object_or_404, render

import random
import string


def code_gen():

    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 6
    return ''.join(random.choice(chars) for num in range(size))






def index(request):

    long_urls = URL.objects.all()
    context = {'long_urls':long_urls}
    
    return render(request, 'short/index.html', context)




def coder(request):
    new_code = code_gen()
    URL.objects.create(pub_date=timezone.now(), url_text=request.POST['url_name'], new_code=new_code)

    return HttpResponseRedirect(reverse('short:index'))


def success(request,short_url):
    
    user_url = get_object_or_404(URL, url_text=short_url)
    new_url = user_url.url_text
    new_url.save()
    return HttpResponseRedirect(new_url)

