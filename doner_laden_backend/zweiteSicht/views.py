from django.shortcuts import render
from django.http import HttpResponse
from .models import Mitarbeiter, Rohe_Produkt
from .forms import KundeForm
from .models import Kunde

# Create your views here.

def registrierungForm(request):
    if request.method == "POST":
        try:
            kunde_name = request.POST['vorname']
            kunde_nachname = request.POST['nachname']
            kunde_usrName = request.POST['benutzer_name']
            email_add = request.POST['email_add']
            pswd = request.POST['pswd']
            Kunde(kunde_name, kunde_nachname, kunde_usrName, email_add, pswd).save()
        except Exception as e:
            messages.success(request, "The usr name is already registered")
    return render(request, 'benuzterSicht/kundenRegistrierung')

def kundeNachBenutzerName(request, usr_name):
    if request.method == "GET":
        kunde = Kunde().objects.get(benutzer_name = usr_name)
        return render(request, 'benuzterSicht/kundenRegistrierung', {'kundeReg': kunde})


def tes_view(request):
    #ls = Mitarbeiter.objects.all().order_by("name")
    fm = KundeForm()
    if request.method == "POST":
        vorname = request.POST['vorname']
        nachname = request.POST['nachname']
        benutzer_name = request.POST['benutzer_name']
        email_add = request.POST['email_add']
        pswd = request.POST['pswd']
        geheim_f = request.POST['gehim_frage']
        geheim_a = request.POST['gehim_answer']
        
        Kunde(vorname=vorname, nachname=nachname, benutzer_name=benutzer_name, email_add=email_add, pswd=pswd).save()
        
    return render(request, 'register.html', {"personen":fm})
    # return HttpResponse("<h1>%s %s %s</h1>" %(ls.name, ls.lastName, ls.address))

def home(request):
    ls = Mitarbeiter.objects.all().order_by("name")
    return render(request, 'home.html', {"personen":ls})
    # return HttpResponse("<h1>%s %s %s</h1>" %(ls.name, ls.lastName, ls.address))

def roheProdukt(request):
    prd = Rohe_Produkt.objects.all()
    return render(request, 'roheProdukt.html', {"roheP":prd})
    # return HttpResponse("<h1>%s %s %s</h1>" %(ls.name, ls.lastName, ls.address))
def benutzerSicht(request):
    return render(request, 'benutzerSicht/index_base.html')
    # return HttpResponse("<h1>%s %s %s</h1>" %(ls.name, ls.lastName, ls.address))