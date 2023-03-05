from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    BASE_PATH = os.getcwd()
    WORK_DRECTORY1 = 'first_project/first_project'
    WORK_DRECTORY2 = 'first_project/app'

    path1 = os.path.join(BASE_PATH, WORK_DRECTORY1)
    list_file_first_project = os.listdir(path1)
    path2 = os.path.join(BASE_PATH, WORK_DRECTORY2)
    list_file_app = os.listdir(path2)
    list_file_first_project.extend(list_file_app)

    msg = f'список файлов в рабочей директори: {list_file_first_project}'
    return HttpResponse(msg)

