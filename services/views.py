from django.shortcuts import render


# Create your views here.

def index(request):
    content = {
        'title': 'Главная',
    }
    return render(request, 'services/index.html', content)


def transcrib(request):
    content = {
        'title': 'Транскрибация'
    }
    return render(request, 'services/transcribation.html', content)


def shop(request):
    content = {
        'title': 'Интернет-магазин',
    }
    return render(request, 'services/shop.html', content)


def parsing(request):
    content = {
        'title': 'Парсинг',
    }
    return render(request, 'services/parsing.html', content)


def telegramm(request):
    content = {
        'title': 'Telegramm бот',
    }
    return render(request, 'services/telegramm.html', content)
