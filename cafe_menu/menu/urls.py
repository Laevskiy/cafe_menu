from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name = 'about'),
    path('contacts/', contacts, name = 'contacts'),
    path('order/', order, name = 'order'),
    path('menu/', main_menu, name = 'main_menu')

]