from django.views.generic import ListView
from coins.models import Coin

class CoinListView(ListView):
    model = Coin
    template_name = 'coins/coin_list.html'
    context_object_name = 'coins'
