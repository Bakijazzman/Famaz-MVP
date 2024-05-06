from django.shortcuts import render # type: ignore
from .models import Item

def index(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'core/home.html', context) 

def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'core/products.html', context)

def checkout(request):
    return render(request, 'core/checkout.html')

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'core/item_list.html', context)