from django.db import models

# Create your models here.
class Stammdaten(models.Model):
    product_name = models.CharField(max_length=250) #Name des Produkts
    unit = models.CharField(max_length=100, default="")#Einheit mit der das Produkt berechnet wird
    storage_temperature = models.IntegerField(default=20)#Temperatur bei das Produkt VOR dem Öffnen gelagert wird
    storage_temperature_open = models.IntegerField(default=20)#Temperatur bei das Produkt NACH dem Öffnen gelagert wird
    durability = models.IntegerField(default=720)#Übliche Haltbarkeit nach dem Kaufen in Tagen default sind zwei Jahre
    durability_open = models.IntegerField(default=720)#Ubliche Haltbarkeit nach dem öffnen, default sind zwei Jahre


class Lagerinhalt(models.Model):
    product = models.ForeignKey(Stammdaten, on_delete=models.CASCADE)#Link zu den Stammdaten
    quantity = models.IntegerField(default=1)#Menge des Produktes in der entsprechenden Einheit
    day_purchased = models.DateField('date purchased') #Tag des Kaufs
    day_opened = models.DateField('date opened')#Tag der Öffnung
