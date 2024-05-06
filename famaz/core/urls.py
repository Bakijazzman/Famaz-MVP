from django.urls import path # type: ignore
from .views import (products, checkout, index, item_list)

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='product'),
    path('checkout/', checkout, name='checkout'),
    path('item_list/', item_list, name='item_list'),
]
