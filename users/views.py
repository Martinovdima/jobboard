from django.shortcuts import render


# Create your views here.
def login(request):
    content = {'title': 'Login'}
    return render(request, 'users/login.html', content)

def register(request):
    content = {'title': 'Registration'}
    return render(request, 'users/register.html', content)