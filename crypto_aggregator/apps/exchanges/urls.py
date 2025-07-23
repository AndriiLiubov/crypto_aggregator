from django.urls import path
from .views import exchange_list

urlpatterns = [
    path('', exchange_list, name='exchange_list'),
]
