from django.urls import path # type: ignore
from .views import (
    ItemDetailView, 
    HomeView,
    remove_from_cart, 
    add_to_cart,
    checkout,
    MyLoginView,
    MySignupView,
    )

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path("checkout/", checkout, name="checkout"),
    path("accounts/login/", MyLoginView.as_view(), name="Login"),
    path("accounts/signup/", MySignupView.as_view(), name="Signup")
]
