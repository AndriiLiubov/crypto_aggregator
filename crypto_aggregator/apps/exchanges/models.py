from django.db import models

class Exchange(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    logo_url = models.URLField(blank=True)
    website = models.URLField()
    commission = models.DecimalField(max_digits=5, decimal_places=2)  # например, 0.10%
    min_deposit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    referral_link = models.URLField(blank=True)
    volume_24h = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

