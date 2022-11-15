from django.db import models

# Create your models here.
class Cnab(models.Model):
    date = models.DateField()
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)

    transaction = models.ForeignKey("transactions.Transaction", on_delete=models.CASCADE, related_name="cnab")