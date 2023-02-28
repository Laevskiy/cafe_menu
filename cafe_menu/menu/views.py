from django.http import HttpResponse
from django.shortcuts import render

#menu = ['Главная','О нас','Меню','Контакты','Сделать заказ']
menu = [ {'name':'Главная','url':'/'},
         {'name':'О нас','url':'/about'},
         {'name':'Меню'},
         {'name':'Контакты', 'url':'/contacts'},
         {'name':'Сделать заказ', 'url':'/order'}

]
menu_v = [{'name':'Салат'},
          {'name':'Супы'},
          {'name':'Горячие блюда'},
          {'name':'Напитки'}]
def home (request):
    return render (request, 'menu/main_page.html',
                   {'title':'Главная страница', 'menu': menu,'menu_v':menu_v})

def about(request):
    return render (request,'menu/about.html',{'title':'Главное меню', 'menu': menu,'menu_v':menu_v})


def main_menu(request):
    return render (request,'menu/main_menu.html',{'title':'Главное меню', 'menu': menu,'menu_v':menu_v})

def contacts(request):
    return render (request,'menu/contacts.html',{'title':'Главное меню', 'menu': menu,'menu_v':menu_v})

def order(request):
    return render (request,'menu/order.html',{'title':'Главное меню', 'menu': menu,'menu_v':menu_v})