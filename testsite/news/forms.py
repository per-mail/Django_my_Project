#Вариант написания формы связанной с моделью
from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

# отправка е-майл
class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))#"rows": 5- размер сообщения
    captcha = CaptchaField()

# логирование на сайте
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# регистрация на сайте
#'autocomplite': "off" - можно добавить параметр параметр отключения автоподстановки
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='До 150 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', help_text='Минимум 8 символов', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User #указываем какую модель будем использовать. Модель User из библиотеки django
        fields = ('username', 'email', 'password1', 'password2')# указываем порядок полей

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        #добавляем сразу все поля
        #fields = '__all__'
        
        #добавляем поля по отдельности
        fields = ['title', 'content', 'is_published', 'category']
        #формирует виджеты на странице?
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }   
   
   #образец валидатора отклоняет заголовки с цифрой в начале
    def clean_title(self):
        title = self.cleaned_data['title']#title прошедший встроенную валидацию 
        if re.match(r'\d', title):# с помощью регулярного выражения проверяем, чтобы в начале заголовка не было цифр
            raise ValidationError('Название не должно начинаться с цифры')
        return title            

