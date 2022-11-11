from django.shortcuts import render

from services.models import Transcrib, ServicesCategory
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def result(request):
    if request.method == "POST":
        aud = Transcrib()
        aud.name = request.POST.get("name")
        aud.audio = request.POST.get("audio_file")
        aud.save()
    return HttpResponseRedirect(reverse('transcrib:index'))


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
