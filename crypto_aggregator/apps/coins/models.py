from django.db import models

class Coin(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    market_cap = models.BigIntegerField(null=True, blank=True)
    volume_24h = models.BigIntegerField(null=True, blank=True)
    percent_change_24h = models.FloatField(null=True, blank=True)
    last_updated = models.DateTimeField()

    def __str__(self):
        return f"{self.name} ({self.symbol.upper()})"
