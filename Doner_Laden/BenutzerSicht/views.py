from django.shortcuts import render
from .forms import KundeForm
from .models import Kunde, GeheimeFA
from django.contrib import messages
# Create your views here.

def benutzerSicht(request):
    #fm = KundeForm()
    # if request.method == 'POST':
    #     kundenForm = KundeForm(request.POST)
    #     if kundenForm.is_valid():
    #         pass  # does nothing, just trigger the validation
    if request.method == "POST":
        fm = KundeForm()
        vorname = request.POST['vorname']
        nachname = request.POST['nachname']
        benutzer_name = request.POST['benutzer_name']
        email_add = request.POST['email_add']
        pswd = request.POST['pswd']
        geheim_f = request.POST['gehim_frage']
        geheim_a = request.POST['gehim_answer']
        se=GeheimeFA(geheime_frage=geheim_f, geheime_antwort=geheim_a)
        kundenForm = KundeForm(request.POST)
        if kundenForm.is_valid():
            se.save()
            Kunde(vorname=vorname, nachname=nachname, benutzer_name=benutzer_name, email_add=email_add, pswd=pswd, geheimeFA=se).save()            
        else:
            return render(request, 'benutzerSicht/index_base.html',{'kundenForm':fm})
    else:
        fm = KundeForm(None)
        return render(request, 'benutzerSicht/index_base.html',{'kundenForm':fm})
    # return HttpResponse("<h1>%s %s %s</h1>" %(ls.name, ls.lastName, ls.address))


def tes_view(request):
    fm = KundeForm()
    #ls = Mitarbeiter.objects.all().order_by("name")
    if request.method == "POST":
        formm = KundeForm(request.POST)
        if formm.is_valid():
            print("Successfull--------------------------------")

    
    # if request.method == "POST":
    #     kunde = KundeForm(request.POST)
    #     if kunde.is_valid():
    #         vorname = request.POST['vorname']
    #         nachname = request.POST['nachname']
    #         benutzer_name = request.POST['benutzer_name']
    #         email_add = request.POST['email_add']
    #         pswd = request.POST['pswd']
    #         geheim_f = request.POST['gehim_frage']
    #         geheim_a = request.POST['gehim_answer']
    #         se=GeheimeFA(geheime_frage=geheim_f, geheime_antwort=geheim_a)
    #         se.save()
    #         Kunde(vorname=vorname, nachname=nachname, benutzer_name=benutzer_name, email_add=email_add, pswd=pswd, geheimeFA=se).save()   
    return render(request, 'register.html', {"personen":fm})
