from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem

def index(request):
    grocery_items = GroceryItem.objects.filter(is_item_completed=False)
    context = {'grocery_items': grocery_items}
    return render(request, 'grocery_app/index.html', context)

def additem(request):
    GroceryItem.objects.create(item_text = request.POST['item_text'])
    return HttpResponseRedirect(reverse('grocery_app:index'))

def completeditem(request, pk):
    selected_item = get_object_or_404(GroceryItem, pk=pk)
    selected_item.is_item_completed = True
    selected_item.save()
    return HttpResponseRedirect(reverse('grocery_app:index'))