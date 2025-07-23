from django.contrib import admin
from .models import Exchange

@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'commission', 'volume_24h')
