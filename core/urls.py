from .views import index, about, login_user, logout_user, register_user, product, category
from django.urls import path


urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path("register/", register_user, name="register" ),
    path("product/<int:pk>", product, name="product"),
    path('category/<str:foo>/', category, name="category"),
]