from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

from services.models import Transcrib, ServicesCategory
from services.forms import TranscribForm

# Create your views here.

def index(request):
    content = {
        'title': 'Главная',
    }
    return render(request, 'services/index.html', content)


def transcrib(request):
    form = TranscribForm()
    content = {
        'title': 'Транскрибация',
        'label_name_services': 'Транскрибация аудио из фалов WAV',
        'form': form,
    }
    return render(request, 'services/transcribation.html', content)

def create(request):
    if request.method == 'POST':
        form = TranscribForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('transcrib:index')
    else:
        form = TranscribForm()
    return render(request, 'services/transcribation.html', {
        'form': form
    })


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
