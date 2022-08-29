from django.db import models
from django.urls import reverse

#поле id формируется автоматически из переопрелённого класса  Model
#при первом запуске модели в последнем поле добавляем default='SOME STRING', потом можно убрать
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Наименование')
    content = models.TextField(blank=True, verbose_name = 'Контент' ) # blank=True - значить поле необязательно для заполнения
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата публикации') # auto_now_add=True - значит время не будет меняться
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Обновлено') # auto_now=True - значит время будет меняться
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name = 'Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, #on_delete=models.PROTECT запрещает удаление данных из первичной модели если на неё есть ссылка во вторичной модели 
verbose_name = 'Категория')
    views = models.IntegerField(default=0, verbose_name = 'Количество просмотров')

#вариант 1
#   def get_absolute_url(self):
#       return reverse('view_news', kwargs={"news_id": self.pk})

#метод get_absolute_url создаёт ссылку на конкректный объект
#get_absolute_url - стандартное название в некоторых случаях django использует его по умолчанию
#вариант 2 работа с классом DetailView
    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})#первый параметр метода reverse название маршрута. второй параметр словарь с идентификатором по которому достаём конкректную новость

#метод возвращает строковое представление обьекта, выводит заголовок в консоле Джанго
#определяем что через поле title будем именовать записи в админке, базе, консоле Джанго

    def __str__(self):
        return self.title

#переводим заголовки в админке на русский
    class Meta:
        verbose_name = 'Новость'        
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']#устанавливаем порядок новостей на обратный по дате добавления 

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name = 'Название категории') #db_index=Ttue - означает что поле индексироввано.  ускоряет работу


    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория' 
        verbose_name_plural = 'Категории'
        ordering = ['title']
