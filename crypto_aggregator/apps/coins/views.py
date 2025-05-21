#from django.shortcuts import render
from django.views.generic import ListView
from apps.coins.models import Coin

class CoinListView(ListView):
    model = Coin
    template_name = 'coins/coin_list.html'
    context_object_name = 'coins'

"""
def coin_list_view(request):
    coins = Coin.objects.all()
    return render(request, 'coins/coin_list.html', {'coins': coins})
"""