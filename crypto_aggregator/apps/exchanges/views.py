from django.shortcuts import render
from .models import Exchange

def exchange_list(request):
    exchanges = Exchange.objects.all().order_by('-volume_24h')
    return render(request, 'exchanges/index.html', {'exchanges': exchanges})

