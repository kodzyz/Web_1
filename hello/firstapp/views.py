# представления -> действия приложений: определение функций, обработка запросов

from django.shortcuts import render
from django.http import HttpResponse  # отправка текстового содержимого

# Create your views here.

def index (request):
    return HttpResponse("<h2>Главная</h2>")

def about (request):
    return HttpResponse("<h2>О Сайте</h2>")

def contact (request):
    return HttpResponse("<h2>Контакты</h2>")

def products (request, productid=1) :  # http://127.0.0.1:8000/products/5/ -> Продукт № 5
    output = f"<h2> Продукт № {productid} </h2"
    return HttpResponse(output)

def users (request, id=1, name="Костя") :  # http://127.0.0.1:8000/users/3/Виктор/
    output = f"<h2> Пользователь </h2> <h3> id:{id} Имя: {name} </h3>"
    return HttpResponse(output)