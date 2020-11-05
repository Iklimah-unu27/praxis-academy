from django.shortcuts import render
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Iwak),
    path('<id>/', views.lihat),
    path('<id>/update', views.ganti),
    path('<id>/delete', views.delete),
]