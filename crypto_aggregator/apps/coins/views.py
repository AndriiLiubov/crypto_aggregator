#from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from apps.coins.models import Coin

class CoinListView(ListView):
    model = Coin
    template_name = 'coins/coin_list.html'  
    context_object_name = 'coins'

def coin_list_json(request):
    coins = Coin.objects.values('id', 'name', 'symbol', 'price', 'percent_change_24h')
    return JsonResponse(list(coins), safe=False)


"""
def coin_list_view(request):
    coins = Coin.objects.all()
    return render(request, 'coins/coin_list.html', {'coins': coins})
"""