from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, SignupForm, EditProfileForm

"""
I have problem on signup 
"""


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home:main')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:main')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_signup(request):
    if request.user.is_authenticated:
        return redirect('home:main')
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('home:main')
    else:
        form = SignupForm()
    return render(request, 'accounts/sign_up.html', {'form': form})

def edit_profile(request):
    form = EditProfileForm(instance=request.user)
    if request.method == 'POST':
        form = EditProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'accounts/edit_profile.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home:main')
