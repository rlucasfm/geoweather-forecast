from django.utils import timezone
from django.db import models

# Create your models here.
class Forecast(models.Model):
    cidade = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, null=True, blank=True)
    temperatura = models.DecimalField(max_digits=12,decimal_places=2, null=True, blank=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.cidade

    def save(self):
        self.timestamp = timezone.now()
        return super().save()