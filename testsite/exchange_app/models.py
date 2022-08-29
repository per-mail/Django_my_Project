from django.db import models
from django.urls import reverse

###, default ='SOME STRING'
##class Exchange(models.Model):
##    sume = models.CharField(max_length=10, verbose_name = 'Сумма обмена')
##    curr = models.ForeignKey('Currencies', on_delete=models.PROTECT, verbose_name = 'Валюта покупки(продажи)')    
##
###метод возвращает строковое представление обьекта, выводит заголовок в консоле Джанго
##    def __str__(self):
##        return self.curr_in    
##
###переводим заголовки в админке на русский
##    class Meta:
##        verbose_name = 'конвертируем валюту'        
##        verbose_name_plural = 'конвертируем валюту'
        
#поле id формируется автоматически из переопрелённого класса  Model
class Currencies(models.Model):
    currencies = models.CharField(max_length=50, db_index=True, verbose_name = 'Валюты')   
    
#метод возвращает строковое представление обьекта, выводит заголовок в консоле Джанго
    def __str__(self):
        return self.currencies



#переводим заголовки в админке на русский
    class Meta:
        verbose_name = 'название валюты'        
        verbose_name_plural = 'название валют'
