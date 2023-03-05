from django.http import HttpResponse
from django.shortcuts import render

from menu.models import *

menu = [ {'name':'Главная','url':'/'},
         {'name':'О нас','url':'/about'},
         {'name':'Меню'},
         {'name':'Контакты', 'url':'/contacts'},
         {'name':'Сделать заказ', 'url':'/order'}

]

menu_v = []
p = Category.objects.all()
for i in p:
    menu_v.append(i)
def home (request):
    return render (request, 'menu/main_page.html',
                   {'title':'Главная страница', 'menu': menu,'menu_v':menu_v})

def about(request):
    return render (request,'menu/about.html',{'title':'Главное меню', 'menu': menu,'menu_v':menu_v})


def main_menu(request):
    p = Category.objects.all()
    return render (request,'menu/main_menu.html',{'title':'Главное меню', 'menu': menu,'menu_v':menu_v,'p':p})

def contacts(request):
    return render (request,'menu/contacts.html',{'title':'Главное меню', 'menu': menu,'menu_v':menu_v})

def order(request):
    return render (request,'menu/order.html',{'title':'Главное меню', 'menu': menu,'menu_v':menu_v})

def main_menu_razdel (request, slug_category):
    cat = Category.objects.filter(slug_category = slug_category)
    number = cat[0].pk
    m = Dishes.objects.filter(name_category_id = number)
    return render (request,'menu/main_menu_razdel.html',{'title':'Главное меню',
                                                         'menu': menu,'menu_v':menu_v,'slug_category':slug_category,
                                                         'm':m, 'number':number})