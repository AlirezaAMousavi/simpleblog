from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home:main')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:main')
    return render(request, 'accounts/login.html', {})


def user_sign_up(request):
    contexts = {'errors': []}
    if request.user.is_authenticated:
        return redirect('home:main')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            contexts['errors'].append('Passwords are different.')
            return render(request, 'accounts/sign_up.html', context=contexts)
        else:
            user = User.objects.create(username=username, password=password1, email=email)
            login(request, user)
            return redirect('home:main')

    return render(request, 'accounts/sign_up.html', {})


def user_logout(request):
    logout(request)
    return redirect('home:main')
