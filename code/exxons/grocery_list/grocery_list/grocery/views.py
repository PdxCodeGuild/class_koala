from django.shortcuts import get_object_or_404,render
from django.urls  import reverse
from django.views import generic
from django.http import HttpResponse
from .models import Item
from django.utils import timezone
 




def index(request):
    grocery_list = Item.objects.all()
    context = {"grocery_list":grocery_list}
    
    return render(request, "grocery/index.html", context)

# def detail(request, question_id):
#     item = get_object_or_404(Item, pk=item_id)
#     return render(request, "grocery/detail.html", {"item": item})