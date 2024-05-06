from django.urls import path # type: ignore
from .views import (products, checkout, index)

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='product'),
    path('checkout/', checkout, name='checkout'),
]
