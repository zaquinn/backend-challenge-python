from django.db import models

# Create your models here.
class Transaction(models.Model):
    description = models.CharField(max_length=25)