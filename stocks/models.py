from django.db import models

# Create your models here.
class Stammdaten(models.Model):
    product_name = models.CharField(max_length=250)
    temperature = models.IntegerField
