from django.shortcuts import render
from .models import Item

def index(request):
    return render(request, 'core/home.html') 

def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'core/products.html', context)

def checkout(request):
    return render(request, 'core/checkout.html')