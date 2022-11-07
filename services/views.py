from django.shortcuts import render

# Create your views here.

def index(request):
    title = 'Главная'
    content = {
        'title': title
    }

    return render(request, 'services/index.html', content)

def transcrib(request):
    title = 'Транскрибация'
    content = {
        'title': title
    }
    return render(request, 'services/transcribation.html', content)

def shop(request):
    title = 'Интернет-магазин'
    content = {
        'title': title
    }
    return render(request, 'services/shop.html', content)

def parsing(request):
    title = 'Парсинг'
    content = {
        'title': title
    }
    return render(request, 'services/parsing.html', content)

def telegramm(request):
    title = 'Telegramm бот'
    content = {
        'title': title
    }
    return render(request, 'services/telegramm.html', content)