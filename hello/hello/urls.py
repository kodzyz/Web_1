"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  # сопоставление запросов с функцией их обработки

from firstapp import views

from django.urls import re_path  # задавать адреса с помощью регулярок

#  переменная urlpatterns определяет набор сопоставлений запросов польз-ля с фу-ями обработки этих запросов
urlpatterns = [

    # параметры строки запроса http://localhost/index?id=3&name=Виктор
    # указываются после (?)
    # параметр (id=3) -> ключ = значение
    # параметры отделяются знаком (&) -> ?id=3&name=Виктор

    path('products/<int:productid>/', views.products),  # http://127.0.0.1:8000/products/3/?cat=Телефоны

    path('users/', views.users),  # http://127.0.0.1:8000/users/?id=8&name=Алексей -> id:8 Имя: Алексей

    path('details/', views.details),  # http://127.0.0.1:8000/details -> http://127.0.0.1:8000/
    path('contact/', views.contact),  # http://127.0.0.1:8000/contact/ -> http://127.0.0.1:8000/about/
    path('about/', views.about),
    path('', views.index),  # http://127.0.0.1:8000/
]

# запуск приложения
# python manage.py runserver
