from django.http import HttpResponse
from django.shortcuts import render

menu = ['Главная','О нас','Меню','Контакты','Сделать заказ']
def home (request):

    return render (request, 'menu/base_menu_001.html', {'title':'Главная страница', 'menu': menu})
