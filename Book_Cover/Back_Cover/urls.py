from django.contrib import admin
from django.urls import path, URLPattern
from . import views

urlpatterns = [
    path('', views.cover, name="cover"),
]