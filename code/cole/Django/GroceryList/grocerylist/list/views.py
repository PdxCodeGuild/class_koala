from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.utils import timezone
from django.urls import reverse

from .models import GroceryItem
# Create your views here.

class itemList(ListView):
    model = GroceryItem
    template_name = 'list.html'

    def get_queryset(self):
        return GroceryItem.objects.order_by('completedDate')


class addItem(CreateView):
    model = GroceryItem
    template_name = 'add.html'
    fields = "itemText", "itemCount"

def complete(request, pk):
    item = get_object_or_404(GroceryItem.objects.all(), pk=pk)
    item.completed = True
    item.completedDate = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('GroceryList:list'))

def uncomplete(request, pk):
    item = get_object_or_404(GroceryItem.objects.all(), pk=pk)
    item.completed = False
    item.completedDate = item.createdDate
    item.save()
    return HttpResponseRedirect(reverse('GroceryList:list'))
