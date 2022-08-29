from django.shortcuts import render, get_object_or_404, redirect

#2 способ с использованием классов ListView, DetailView, CreateView
from django.views.generic import ListView, DetailView, CreateView




from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm

#пример с миксинами
from .utils import MyMixin

from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail





#регистрация на сайте
def register(request):
    if request.method == 'POST':# если данные пришли методом POST
        form = UserRegisterForm(request.POST)# создаём форму и передаём в неё данные
        if form.is_valid():# если форма валидная
            user = form.save()# сохраняем форму, получаем пользователя
            login(request, user)#передаём пользователя в метод login()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')#после регистрации на сайте перенаправляем пользователя на главную страницу
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()# создаём объект формы не связанный с данными
    return render(request, 'news/register.html', {"form": form})

# логирование на сайте
def user_login(request):
    if request.method == 'POST':# если данные пришли методом POST
        form = UserLoginForm(data=request.POST)#создаём форму и передаём в неё данные
        if form.is_valid(): # если форма валидная
            user = form.get_user()# получаем пользователя методом get_user()
            login(request, user)#передаём пользователя в метод login()
            return redirect('home')#после логирования перенаправляем пользователя на главную страницу
    else:
        form = UserLoginForm()# создаём объект формы не связанный с данными
    return render(request, 'news/login.html', {"form": form})

# выходим из логина
def user_logout(request):
    logout(request)
    return redirect('login')#перенаправляем пользователя на страницу авторизации

# отправка е-майл
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #сохрняем данные в переменную mail
            #form.cleaned_data['subject'] берём данные из subject
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], '', [''], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = ContactForm()
    return render(request, 'news/test.html', {"form": form})


#2 способ с использованием класса ListView
class HomeNews(MyMixin, ListView):
    model = News# берём модель News
    template_name = 'news/news_list.html'# подключаем нужный html-файл
    context_object_name = 'news'# указываем что мы используем объект news здесь и в шаблоне news_list.html  {% for item in news %}
    #extra_context = {'title': 'Главная'}# этот способ годится только для статичных методов

    #пример с миксинами
    mixin_prop = 'пример с миксинами'
    
#создаём пагинацию 2 способ с помощью класса ListView, где 2 это количество новостей на странице
    paginate_by = 2
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)# берём данные из существующего context
        #пример с миксинами self.get_upper - приводит строку к верхнему регистру
        context['title'] = self.get_upper('Главная страница')#добавляем в существующий context данные
        #пример с миксинами
        context['mixin_prop'] = self.get_prop()
        return context
    
# с помощью этого кода .select_related('category') уменьшаем количество запросов к базе данных
# т. е. при запросе к базе данных выбираем только поля у которых is_published=True
    def get_queryset(self):                                                      #select_related - с помощью этого метода мы просим Джанго загружать данные не отложено я сразу же при получении новостей
        return News.objects.filter(is_published=True).select_related('category')#select_related('category') - с помощью этого метода оптимизируем количество запрсов к бд
                                                                                # select - название модели которую оптимизируем
#2 способ с использованием класса ListView
# используем тот же шаблон, что и главная страница        
class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    allow_empty = False #с помощью этого метода запрещаем открывать страницы пустых категорий
#создаём пагинацию 2 способ с помощью класса ListView, где 2 это количество новостей на странице
    paginate_by = 2 #2 кол-во записей выводимые на страницу
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #пример с миксинами self.get_upper
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))  #с помощью category_id  получаем данные текущей категории    
        return context


