# представления -> действия приложений: определение функций, обработка запросов

from django.shortcuts import render
from django.http import HttpResponse  # отправка текстового содержимого

# Create your views here.

def index (request):
    return HttpResponse("Hello World! Это мой первый проэкт на Dlango!")  # создание ответа пользователю
