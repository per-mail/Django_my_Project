from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())#для content переопределяем форму редактораCKEditor 
# переопределяем модель News
    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
# создаёт кнопку сохранить как новый обьект
    save_as = True
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')# определяем поля для поиска.
    list_editable = ('is_published',)# определяем поля которые будут редактироваться
    list_filter = ('is_published', 'category')# определяем поля для фильтра
# определяем поля в форме создания новости
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'views', 'is_published', 'created_at', 'updated_at')
# определяем поля только для чтения, не будут редактироваться
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')
# создаём две панели редактирования в админке вверху и внизу
    save_on_top = True
    
#возвращаем путь к картинке. Выводим картинку в панели админки
    def get_photo(self, obj):
        if obj.photo:# если есть фото в обьекте
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'# меняем заголовок по умолчанию get_photo на Миниатюра

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

#регистрируем моделей в админке
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
