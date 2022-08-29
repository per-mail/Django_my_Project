from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *



urlpatterns = [
    #функция path
    #'register/'-маршрут (ссылка)
    #register - функция которая обрабатывает запрос
    path('register/', register, name='register'),#name - имя маршрута задаём здесь, чтобы использовать в шаблонах для построения ссылок 
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact/', contact, name='contact'),
    #path('exchange/', add_exchange, name='add_exchange'),
    #создаём пагинацию 1 способ с помощью функции
    #path('test/', test, name='serf'),
    
    #path('', index),
    #path('category/<int:category_id>/', get_category),    

    #вариант 1
    #path('', index, name='home'),
    

    #вариант 2 работа с классом ListView
    #''-маршрут (ссылка) здесь 'news/'- не пишем, это первая ссылка ведущая в приложение
    #HomeNews - класс который обрабатывает запрос
    #as_view() - метод импортируемый из суперкласса
    path('', HomeNews.as_view(), name='home'),

    #вариант 2 работа с классом ListView с кешированием
    #path('', cache_page(60)(HomeNews.as_view()), name='home'),
    
    #вариант 1
    #path('category/<int:category_id>/', get_category, name='category'),
    
    #вариант 2 работа с классом ListView
    #'category/<int:category_id>/'-маршрут (ссылка)    
    #<int:category_id> - получаем номер категории
    #NewsByCategory.as_view(() - класс обработчик запроса
    #as_view() - метод импортируемый из суперкласса, с помощью него можно передавать параметры
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title':'Так можно передавать параметры'}), name='category'),
    
    #вариант 1
    #path('news/<int:news_id>/', view_news, name='view_news'),
    
    #вариант 2 работа с классом DetailView
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    
    #вариант 1
    #path('news/add-news>/', add_news, name='add_news'),

    #вариант 2 работа с классом CreateView
    path('news/add-news>/', CreateNews.as_view(), name='add_news'),
]

