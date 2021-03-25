from django.shortcuts import render
from .forms import KundeForm, GeheimFAForm, LoginForm
from .models import Kunde, GeheimeFA
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def Login(request, loginForm):
    
    if loginForm.is_valid():
        pass
    #return render(request, 'benutzerSicht/index_base.html',{'loginForm':loginForm})

def Registration(request, regForm, regGFA):
    if regForm.is_valid() and regGFA.is_valid():
            vorname = request.POST['vorname']
            nachname = request.POST['nachname']
            benutzer_name = request.POST['benutzer_name']
            email_add = request.POST['email_add']
            pswd = request.POST['pswd']
            geheimTabelle = regGFA.save()
            Kunde(vorname=vorname, nachname=nachname, benutzer_name=benutzer_name, email_add=email_add, pswd=pswd, geheimeFA=geheimTabelle).save()

def benutzerSicht(request):
    regForm = KundeForm(data =request.POST)
    regGFA = GeheimFAForm(data =request.POST)
    loginForm = LoginForm(data = request.POST)
    
    if 'registration' in request.POST:
        
        # if request.method == 'POST':
        #     kundenForm = KundeForm(request.POST)
        #     if kundenForm.is_valid():
        #         pass  # does nothing, just trigger the validation
        Registration(request, regForm, regGFA)

        # geheimTabelle = regGFA.save()
        # kundeTabelle = regForm.save(commit=False)
        # kundeTabelle.geheimeFA = geheimTabelle
        # kundeTabelle.save()
    elif 'login' in request.POST:
        Login(request, loginForm)
    return render(request, 'benutzerSicht/index_base.html',{'regForm':regForm,'regGFA': regGFA, 'loginForm': loginForm})
