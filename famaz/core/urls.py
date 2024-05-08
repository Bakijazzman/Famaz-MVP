from django.urls import path # type: ignore
from .views import (ItemDetailView, checkout, HomeView, item_list)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('checkout/', checkout, name='checkout'),
    path('item_list/', item_list, name='item_list'),
]
