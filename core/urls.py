from .views import update_user, login_user, logout_user, register_user
from .views import product, category, category_summary, index, about
from django.urls import path


urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path("register/", register_user, name="register" ),
    path("update_user/", update_user, name="update" ),
    path("product/<int:pk>", product, name="product"),
    path('category/<str:foo>', category, name="category"),
    path('category_summary', category_summary, name="category_summary"),
]