from django.shortcuts import render

# Create your views here.

def index(request):
    title = 'Главная'
    content = {
        'title': title
    }

    return render(request, 'services/index.html', content)

def transcrib(request):
    title = 'Трнаскрибация'
    content = {
        'title': title
    }
    return render(request, 'services/transcribation.html', content)