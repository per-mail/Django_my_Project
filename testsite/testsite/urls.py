"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#  нужно только при работе в отладочном режиме
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    #ссылка на админку даётся по умолчанию
    path('admin/', admin.site.urls),
    #с помощью функции include() передаём в корневой маршрутизатор список маршрутов из файл urls в приложении news
    path('news/', include('news.urls')),
    #стандартный маршрут берём из библиотеки редактора текста
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #стандартный маршрут берём из библиотеки капчи
    path('captcha/', include('captcha.urls')),


    
#конвертер валют
    path('exchange/', include('exchange_app.urls')),
    
]

#  нужно только при работе в отладочном режиме. маршрут для сохранения графических файлов статических файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

