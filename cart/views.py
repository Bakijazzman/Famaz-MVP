from django.shortcuts import render, get_object_or_404
from .cart import Cart
from core.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prod
    quantities = cart.get_quants
    return render(request, 'cart_summary.html', {"cart_products":cart_products, "quantities":quantities})


def cart_add(request):
    #Gett cart
    cart = Cart(request)
    #test for post
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        #get cart qunatity
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty: ': cart_quantity})
        messages.success(request, ("Product Added To Cart..."))
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response =JsonResponse({'product': product_id})
        messages.success(request, ("Item removed, you can re-add at the product page"))
        return response
    
    
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)
        response =JsonResponse({'qty': product_qty})
        messages.success(request, ("Your Cart Has Been Updated... reload page to see changes "))
        return response
        #return redirect('cart_summary')
