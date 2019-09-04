from django.shortcuts import get_object_or_404,render
from django.urls  import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from django.utils import timezone
 




def index(request):
    incomplete_list = Item.objects.filter(is_complete = False)
    complete_list = Item.objects.filter(is_complete = True)
    context = {"incomplete_list":incomplete_list, "complete_list": complete_list}
    
    return render(request, "grocery/index.html", context)

def items(request):
    
    Item.objects.create(created_date=timezone.now(), item_text=request.POST['item_name'])
    
    return HttpResponseRedirect(reverse('grocery:index'))

def delete_item(request,pk):
    item = get_object_or_404(Item, pk=pk)
    
    if request.method == 'POST':
        item.delete()
    
    return HttpResponseRedirect(reverse('grocery:index'))

def complete_items(request,pk):
    item = get_object_or_404(Item, pk=pk)
    
    if request.method == 'POST':
        item.is_complete = True
        item.save()
    
    return HttpResponseRedirect(reverse('grocery:index'))
    




    

# def detail(request, question_id):
#     item = get_object_or_404(Item, pk=item_id)
#     return render(request, "grocery/detail.html", {"item": item})