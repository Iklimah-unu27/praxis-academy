from django.shortcuts import render
from django.urls import path

from . import views

urlpatterns = [
     path('', views.Penjual),
     path('<id>/', views.view),
     path('<id>/update', views.ubah),
     path('<id>/delete', views.delete),
]