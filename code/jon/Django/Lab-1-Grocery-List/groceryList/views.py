from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import GroceryItem
from django.utils import timezone

def index(request):
    current_grocery_list = GroceryItem.objects.filter(is_completed = False)
    bought_grocery_list = GroceryItem.objects.filter(is_completed = True)
    context = {'current_grocery_list':current_grocery_list, 'bought_grocery_list':bought_grocery_list} 
    return render(request, 'groceryList/index.html', context)

def add(request):
    GroceryItem.objects.create(grocery_item=request.POST['grocery_item'])
    return HttpResponseRedirect(reverse('groceryList:index'))

def completed(request, pk):
    complete = get_object_or_404(GroceryItem, pk=pk)
    complete.is_completed = True
    # complete.completed_date = timezone.now
    complete.save()
    return HttpResponseRedirect(reverse('groceryList:index'))

def delete(request):
    GroceryItem.objects.filter(is_completed=True).delete()
    return HttpResponseRedirect(reverse('groceryList:index'))
