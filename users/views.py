from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import *

# Create your views here.


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('core:home')
            else:
                return render(request, 'authentication/login.html', {"form": form, "error": "Invalid Login. User does not exist."})

    form = LoginForm()
    return render(request, 'authentication/login.html', {"form": form})


def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth_login(request, user)  # Correct usage of login
                return redirect('core:home')
    else:
        form = SignUpForm()
    return render(request, 'authentication/signUp.html', {"form": form})

def logout(request):
    auth_logout(request)
    return redirect('users:login')