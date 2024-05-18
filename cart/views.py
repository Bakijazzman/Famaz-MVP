from django.shortcuts import render, get_object_or_404
from .cart import Cart
from core.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    return render(request, 'cart_summary.html', {})


def cart_add(request):
    #Gett cart
    cart = Cart(request)
    #test for post
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        #get cart qunatity
        cart_quantity = cart.__len__()
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty: ': cart_quantity})
        messages.success(request, ("Product Added To Cart..."))
        return response


def cart_delete(delete):
    pass
    
    
def cart_update(request):
    pass
