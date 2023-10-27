from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, UserProfileForm
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Замените 'home' на URL вашей главной страницы
            else:
                messages.error(request, 'Неправильные учетные данные')
        else:
            messages.error(request, 'Неправильные учетные данные')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически войти в систему после регистрации
            return redirect('home')  # Замените 'home' на URL вашей главной страницы
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    form = UserProfileForm(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        # Добавьте другие поля, которые вы хотите включить в профиль пользователя
    })

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

    return render(request, 'profile.html', {'form': form})