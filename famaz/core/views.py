from django.shortcuts import render # type: ignore
from .models import Item
from django.views.generic import ListView, DetailView

class HomeView(ListView):
    model = Item
    template_name = "core/home.html"
    

class ItemDetailView(DetailView):
    model = Item
    template_name = "core/product.html"
    
    
# def products(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, 'core/products.html', context)

def checkout(request):
    return render(request, 'core/checkout.html')

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'core/item_list.html', context)