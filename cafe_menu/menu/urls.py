from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name = 'about'),
    path('contacts/', contacts, name = 'contacts'),
    path('order/', order, name = 'order'),
    path('menu/', main_menu, name = 'main_menu'),
    path('menu/<slug:slug_category>/', main_menu_razdel, name = 'main_menu_razdel'),

]