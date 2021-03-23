from django.db import models

#Create your models here.
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

class Mitarbeiter(models.Model):
    name = models.TextField()
    lastName = models.TextField()
    address = models.TextField()
    position = models.TextField(default='This is not cool')

class Rohe_Produkt(models.Model):
    name = models.CharField(max_length=200)
    produkt_art = models.CharField(max_length=200)
    anzahl = models.PositiveIntegerField()
    beschreibung = models.TextField()

    def __str__(self):
        return self.name

    def snippet(self):
        return self.beschreibung[:50] + '...'

class Addresse(models.Model):
    stadt = models.CharField(max_length=200)
    pstl_zahl = models.PositiveIntegerField()
    strasse =  models.CharField(max_length=300)
    haus_nr = models.PositiveIntegerField()
class Bestellungen(models.Model):
    bestellung_nummer = models.PositiveIntegerField()
    bestellung_name = models.CharField(max_length=200)
    bestellung_anzahl = models.PositiveIntegerField()
    bestellung_zeit = models.DateField()
    liefer_add = Addresse()
    extra_wuensche = models.TextField()

