from django.urls import path
from . import views

app_name = 'apps.coins'

urlpatterns = [
    path('', views.CoinListView.as_view(), name='CoinListView')
]