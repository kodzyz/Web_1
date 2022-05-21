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

    # параметры ф-и path() -> <спецификатор(int, str, slug, uuid, path): название_параметр>

    path('products/<int:productid>/', views.products),  # http://127.0.0.1:8000/products/5/

    path('products/', views.products),  # маршрут по умолчанию (productid=1) http://127.0.0.1:8000/products/

    path('users/<int:id>/<name>/', views.users),  # http://127.0.0.1:8000/users/3/Виктор/

    path('users/', views.users),  # маршрут по умолчанию (id=1, name="Костя") http://127.0.0.1:8000/users/

    re_path(r'contact/', views.contact),
    re_path(r'^about', views.about),
    path('', views.index),
]

# запуск приложения
# python manage.py runserver
