from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.WeatherApi.as_view()),
]