from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm


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
    content = {'title': 'Registration'}
    return render(request, 'users/register.html', content)