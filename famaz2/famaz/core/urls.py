from .views import index, about, login_user, logout_user
from django.urls import path


urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]