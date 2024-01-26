from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from .forms import *


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Проверка наличия пользователя с указанным логином
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Пользователь с таким логином уже существует.')
                return render(request, 'accounts/signup.html', {'form': form})

            # Проверка наличия пользователя с указанным электронным адресом
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Пользователь с таким адресом электронной почты уже зарегистрирован.')
                return render(request, 'accounts/signup.html', {'form': form})

            user = form.save()
            login(request, user)
            return redirect('home')  # Предполагается, что у вас есть URL-шаблон с именем 'home'
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page or any desired page after login
            else:
                # Handle incorrect login credentials
                return render(request, 'accounts/login.html',
                              {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
