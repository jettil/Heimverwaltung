# Register your models here
from django.contrib import admin
from .models import Stammdaten
from .models import Lagerinhalt

admin.site.register(Stammdaten)
admin.site.register(Lagerinhalt)