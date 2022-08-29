#видео: https://www.youtube.com/watch?v=MEBcXMn58zE&list=PLmC7X4gkQWCeyIdLxHZdts-3tkcrxP4-o&index=20
# пользовательские тэги нужны, чтобы убрать дублирование кода.
from django import template
from django.db.models import Count, F
from django.core.cache import cache

from news.models import Category

# регистрируем тэги
register = template.Library()

# тэг возвращает список категорий на странице
@register.simple_tag(name='get_list_categories')#name='get_list_categories'-переименовываем тэг
def get_categories():
    return Category.objects.all()# возвращаем все категории

# тэг получает и показывает список категорий
@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='так можно', arg2='выводить символы'):
 #кэширование категорий убираем на этапе разработки , чтбы видеть актуальные данные
    # берём категории из кеша
    # categories = cache.get('categories')
    # if not categories: # если категорий нет в кеш берём их из бд и кешируем на 30 сек
    #     categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    #     cache.set('categories', categories, 30)
    
    # filter=F('news__is_published')-отбираем опубликованные статьи
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return {"categories": categories, "arg1": arg1, "arg2": arg2}
