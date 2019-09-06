from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import GroceryItem

def index(request):
    current_grocery_list = GroceryItem.objects.filter(is_completed = False)
    bought_grocery_list = GroceryItem.objects.filter(is_completed = True)
    context = {'current_grocery_list':current_grocery_list, 'bought_grocery_list':bought_grocery_list} 
    return render(request, 'groceryList/index.html', context)

def add(request):
    GroceryItem.objects.create(grocery_item=request.POST['grocery_item'])
    return HttpResponseRedirect(reverse('groceryList:index'))

# def complete(request, pk):
    