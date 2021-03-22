from django.contrib import admin

from .models import Mitarbeiter, Rohe_Produkt

# Register your models here.

admin.site.register(Mitarbeiter)

admin.site.register(Rohe_Produkt)