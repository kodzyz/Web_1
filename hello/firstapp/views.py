# представления -> действия приложений: определение функций, обработка запросов

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect  # временная и постоянная переадресация

# Create your views here.

def index (request):
    return HttpResponse("Index")

def about (request):
    return HttpResponse("About")

# временная -> перенаправление по пути "about" что обрабатывается ф-й about
def contact (request):
    return HttpResponseRedirect("/about")  # http://127.0.0.1:8000/contact/ -> http://127.0.0.1:8000/about/

# постоянная переадресация в "корень"
def details (request):
    return HttpResponsePermanentRedirect("/")  # http://127.0.0.1:8000/details -> http://127.0.0.1:8000/

# получение параметров из строки запроса метод -> request.GET.get()

def products (request, productid) :  # http://127.0.0.1:8000/products/3/?cat=Телефоны
    category = request.GET.get("cat", "")  # ("название параметра строки запроса", "значение по умолчанию")
    output = f"<h2> Продукт № {productid} Категория: {category} </h2"
    return HttpResponse(output)  # -> Продукт № 3 Категория: Телефоны

def users (request) :  # http://127.0.0.1:8000/users/?id=8&name=Алексей
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Костя")
    output = f"<h2> Пользователь </h2> <h3> id:{id} Имя: {name} </h3>"
    return HttpResponse(output)