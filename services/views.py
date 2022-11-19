from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
import os  # Библиотека для работы с системой
import time  # Библиотека для работы со временем
import speech_recognition as sr  # Библиотека с популярными сервисами распознавания речи
from pydub import AudioSegment  # Библиотека для работы с аудиоданными
from jobboard.settings import BASE_DIR

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

def split_sound(file, view=False):
    sound = AudioSegment.from_wav(file)  # Считываем звуковой файл
    len_sound = len(sound)  # Узнаем размер айдио файла в милисекундах
    if view:  # Если условие view равняется True
        print(
            f'Audio file size: {(len_sound / 1000) // 60} min. {(len_sound - (((len_sound / 1000) // 60) * 60000)) // 1000} sec.')  # Отображаем размер аудиофайла
    step = 60000  # Определяем шаг среза в 1 минуту
    chunks = []  # Создаем пустой список для аудиофрагментов
    for i in range(0, len_sound, step):  # Проходим по рамеру файла с шагом в минуту
        chunks.append(sound[i: step + i])  # Производим срез файла по минутно
    if view:  # Если условие view равняется True
        print(f'Count files {len(chunks)}')  # Отображаем количество созданных аудиофрагментов
    return chunks

def conversion(filename, id):
    os.chdir('media')
    try:
        os.mkdir('transcrib_text{0}'.format(id))  # Создаем директорию для аудиофайлов
    except(FileExistsError):
        pass  # Если директория уже существует, то пропускаем
    os.chdir('transcrib_text{0}'.format(id))  # Переходим в ранее созданную директорию

    f = open("decoded{0}.txt".format(id), "w+")  # Открываем файл текстовый на запись
    chunks = split_sound(filename, view=True)  # Разрезаем аудиофайл на фрагменты
    try:
        os.mkdir('audio_chunks')  # Создаем директорию для аудиофайлов
    except(FileExistsError):
        pass  # Если директория уже существует, то пропускаем
    os.chdir('audio_chunks')  # Переходим в ранее созданную директорию

    for i, chunk in enumerate(chunks):  # Пробегаем по всем аудиофрагментам
        chunk_silent = AudioSegment.silent(duration=1000)  # Создаем фрагмент тишины размером в 1 секунду
        audio_chunk = chunk_silent + chunk + chunk_silent  # Добавляем вначало и конец файлы тишины для лучшего определения
        print("Saving chunk{0}.wav".format(i))  # Отображаем процесс сохранения файла
        audio_chunk.export(".//chunk{0}.wav".format(i), bitrate='192k', format="wav")  # Сохраняем аудиофайл
        file = 'chunk' + str(i) + '.wav'  # Выбираем сохраненный файл
        print("Processing chunk " + str(i))  # Отображаем процесс преобразования

        r = sr.Recognizer()  # Объявляем класс считывателя
        with sr.AudioFile(file) as source:
            r.adjust_for_ambient_noise(source) #Удаляем лишний шум
            audio_listened = r.listen(source)  # Чтение аудиофайла

        try:
            rec = r.recognize_google(audio_listened, language='ru')  # Конвертируем аудио в текст
            f.write(rec + ". ")  # Записываем текст в файл
            print("Successful chunk " + str(i))  # Отображаем положительный результат

        except sr.UnknownValueError:
            print("Could not understand audio")  # Если в аудиофайле нет речи

        except sr.RequestError as e:
            print(
                "Could not request results. check your internet connection")  # Если отсутствует подключение к интернету
    print(f'Conversion finished!')  # Отображении о завершении конвертации
    os.chdir('..')  # Закрываем директорию
    return os.path.join(BASE_DIR, 'media/transcrib_text{0}/decoded{0}.txt'.format(id, id))
    #return f'Conversion finished!'

def create(request):
    if request.method == 'POST':
        form = TranscribForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.save()
            new_file.text = conversion(request.FILES['audio'], new_file.id)
            new_file.save()
            form.save_m2m()
            return redirect('transcrib:transcribation_result')
    else:
        form = TranscribForm()
    return render(request, 'services/transcribation.html', {
        'form': form
    })

def transcribation_result(request):
    files = Transcrib.objects.all()
    content = {
        'title': 'Результат транскрибации',
        'files': files
    }
    return render(request, 'services/transcribation_result.html', content)

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
