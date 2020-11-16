
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import *
from .forms import CreateUserForm

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/account/')
			else:
				print(form.errors)
		context = {'form':form}
		return render(request, 'account/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('account/home.html')
	else:
		if request.method == 'POST':
			username =request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)
            return redirect(request, 'home')
			if user is not None:
				login(request, user)
				return redirect('register')

			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'account/login.html', context)

def homePage(request):
    return render(request, 'account/home.html')

def logoutUser(request):
	logout(request)
	return redirect('/account/')