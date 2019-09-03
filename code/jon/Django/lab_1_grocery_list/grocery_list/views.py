from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import GroceryItem

def index(request):
    # return HttpResponse('<h1>Grocery List</h1>')
    # grocery_text = GroceryItem.objects.order_by(-created_date)
    # context = {'grocery_text' : grocery_text}
    return render(request, 'grocery_list/index.html')
    
def add(request):
    GroceryItem.objects.create(grocery_text = 'request.POST[grocery_text]', created_date = 'request.POST[created_date]', is_completed = False)
    return HttpResponseRedirect(reverse('grocery_list:index'))


