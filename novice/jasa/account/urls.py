from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),
	path('home/', views.homePage, name="home"),
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
]