from django.shortcuts import render
from django.urls import path

from . import views

urlpatterns = [
     path('', views.Penjual),
#     path('<id>/', views.detail),
#     path('<id>/update', views.edit),
#     path('<id>/delete', views.delete),
]