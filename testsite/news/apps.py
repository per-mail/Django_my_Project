from django.apps import AppConfig

#переводим заголовок в админке на русский
class NewsConfig(AppConfig):
    name = 'news'
    verbose_name= 'Новости'
