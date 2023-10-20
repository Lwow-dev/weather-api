from django.contrib import admin
from django.urls import path, include
import weatherapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weatherapi.urls')),
]
