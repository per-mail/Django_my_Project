#Вариант написания формы связанной с моделью
from django import forms
from .models import*
import re

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from captcha.fields import CaptchaField
from .models import*

import requests


### конвертация вариант написания формы связанной с моделью 
##class ExchangeForm(forms.ModelForm):
##     class Meta:
##        model = Exchange
##        
##       #добавляем поля по отдельности
##        fields = ['sume', 'curr', 'curr']
##        #формирует виджеты на странице?
## 
        #captcha = CaptchaField()

#Вариант написания формы несвязанной с моделью
class ExchangeForm(forms.Form): 
    sume = forms.IntegerField(label='Сумма продажи')
    curr_in = forms.ModelChoiceField(label='Валюта продажи', queryset=Currencies.objects.all(), widget=forms.Select(
    attrs={
       "class": "form-control"      
    }))    
    curr_out = forms.ModelChoiceField(label='Валюта покупки', queryset=Currencies.objects.all(), widget=forms.Select(
    attrs={
       "class": "form-control"      
    })) 
    
    #rez = forms.CharField(max_length=50, label='Результат', required=False)# required=False поле не обязательно для заполнения
    captcha = CaptchaField()


class ExchangeRezForm(forms.Form): 
    sume = forms.CharField(max_length=50, label='Сумма продажи')
    curr_in = forms.CharField(max_length=50, label='Валюта продажи')
    curr_out = forms.CharField(max_length=50, label='Валюта покупки')
    rez = forms.CharField(max_length=50, label='Суммa покупки')
   
