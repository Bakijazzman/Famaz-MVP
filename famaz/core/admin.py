from django.contrib import admin # type: ignore

# Register your models here.
from .models import Item, Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Item)