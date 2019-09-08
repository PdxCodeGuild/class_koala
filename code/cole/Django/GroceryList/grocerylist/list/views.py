from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.

def new_item(request):
    return HttpResponse(GroceryItem.itemText)
