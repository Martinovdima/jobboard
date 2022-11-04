from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'services/index.html')

def transcrib(request):
    return render(request, 'services/transcribation.html')