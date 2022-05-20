# представления -> действия приложений: определение функций, обработка запросов

from django.shortcuts import render
from django.http import HttpResponse  # отправка текстового содержимого

# Create your views here.

#ф-и для выдачи заголовков трех страниц
def index (request):
    return HttpResponse("<h2>Главная</h2>")

def about (request):
    return HttpResponse("<h2>О Сайте</h2>")

def contact (request):
    return HttpResponse("<h2>Контакты</h2>")