from django.views.generic import CreateView
from django.shortcuts import render

from .forms import*
import requests

###конвертируем валюту вариант с  классом CreateView
##class CreateExchange(CreateView):
##    form_class = ExchangeForm # указываем нужную форму
##    template_name = 'exchange_app/exchange.html'# указываем нужный html-файл
##    raise_exception = True# показывает ошибку 403 пользователям если нет прав добавления новости
##   
           

    
# конвертируем валюту вариант с функцией
def add_exchange(request):
    #делаем запрос к api
    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    #получаем словарь  с ключами название валюты и значениеми их стоимость относительно доллара
    #сохраняем результат в переменную currencies
    currencies = response.get('rates')    


###формируем ответ файл index.html с данными из словаря context
##        return render(request, 'exchange_app/exchange.html', {"form": form})
    
    if request.method == 'POST':# если пользователь ввёл данные в таблицу
        form = ExchangeForm(request.POST)
        if form.is_valid(): # если форма валидная

# забираем данные из формы         
            sume = float(form.cleaned_data['sume'])#получаем введённое число переводим в строоковый формат так-как ключ в словаре строка
            curr_in = str(form.cleaned_data['curr_in'])#получаем валюту которую меняем          
            curr_out = str(form.cleaned_data['curr_out'])#получаем валюту на которую меняем
                        
###делаем  конвертацию результат округляем до второго знака после запятой
###из словаря currencies берём значения валют, значение валюты которую меняем  делим на значение валюты на которую меняем и умножаем на введённое число преведённое в дробную форму
            rez = round((currencies[curr_out] / currencies[curr_in]) * float(sume), 2)

#передаём результат в форму
            ent = {                                       
                    'sume': sume, #необходимо передать для того чтобы заполненные значения полей не сбрасывались
                    'curr_in': curr_in,#необходимо передать для того чтобы заполненные значения полей не сбрасывались
                    'curr_out': curr_out,#необходимо передать для того чтобы заполненные значения полей не сбрасывались           
                    'rez': rez
            }
           
            form = ExchangeRezForm(ent)
            return render(request, 'exchange_app/exchange_rez.html', {"form": form})
            #return render(request, 'exchange_app/ExchangeResult.html', ent)

#создаём форму для ввода данных
    else:
        form = ExchangeForm()
        return render(request, 'exchange_app/exchange.html', {"form": form})

