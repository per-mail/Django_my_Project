from django.urls import path
from .views import *

urlpatterns = [
    path('', add_exchange, name='add_exchange'),    
]
