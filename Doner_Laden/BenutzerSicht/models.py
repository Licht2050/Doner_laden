from django.db import models

# Create your models here.

class GeheimeFA(models.Model):
    geheime_frage = models.TextField()
    geheime_antwort = models.TextField()

class Kunde(models.Model):
    vorname = models.CharField(max_length=200)
    nachname =  models.CharField(max_length=200)
    benutzer_name = models.CharField(max_length=200)
    email_add = models.EmailField()
    pswd = models.CharField(max_length=300)
    geheimeFA = models.OneToOneField(GeheimeFA, on_delete=models.CASCADE, related_name='kundenInfo')
