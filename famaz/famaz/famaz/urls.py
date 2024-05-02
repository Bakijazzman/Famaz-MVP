
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore

from core.views import index
urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]
