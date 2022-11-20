from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth, messages
from django.urls import reverse

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    content = {'title': 'Login', 'form': form}
    return render(request, 'users/login.html', content)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    content = {'title': 'Registration', 'form': form}
    return render(request, 'users/register.html', content)


def profile(request):
    form = UserProfileForm(instance=request.user)
    content = {'title': 'Личный кабинет', 'form': form}
    return render(request, 'users/profile.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))