from django.core.exceptions import ValidationError
from django import forms
from .models import Kunde, GeheimeFA
from django.contrib.auth import authenticate



class KundeForm(forms.ModelForm):
    vorname = forms.CharField(max_length=200, label='Vorname', widget=forms.TextInput(attrs={'class': 'form-control'}))
    nachname = forms.CharField(max_length=200, label='Nachname', widget=forms.TextInput(attrs={'class': 'form-control'}))  
    benutzer_name = forms.CharField(max_length=200, label='Benutzername', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email_add = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    pswd = forms.CharField(label='Kennwort',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    pswd_wdh = forms.CharField(label='Wiederhole Kennwort', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    #password felder mit einander vergleichen.
    # def clean(self):
    #     valpswd = self.cleaned_data['pswd']
    #     valpswd_wdh = self.cleaned_data['pswd_wdh']
    #     if valpswd != valpswd_wdh:
    #         raise forms.ValidationError('kennwort stimmen nicht ueberein!')

    class Meta:
        model = Kunde
        fields = ["vorname", "nachname", "benutzer_name", "email_add", "pswd"]
    
    # def clean_pswd(self):
    #     pswd = self.cleaned_data.get('pswd')
    #     if len(pswd) < 8:
    #         #self.errors['pswd'] = self.error_class(['kennwort stimmen nicht ueberein!'])
    #         raise forms.ValidationError("kennwort stimmen nicht ueberein!") 
    #     return pswd
    def clean_benutzer_name(self):
        eingabe = self.cleaned_data.get('benutzer_name')
        if eingabe is not None:
            try:
                hilf = Kunde.objects.get(benutzer_name=eingabe)
                if hilf is None:
                    print("Test False----------------- ")
                    return eingabe
                else:
                    print("Benutzer existiert----------------- ")
                    raise forms.ValidationError("Test False----------------- ")
            except:
                print("Benutzer existiert----------------- ")
                raise forms.ValidationError("Test False----------------- ")
        else:
            raise forms.ValidationError("Benutzer Name darf nicht leer sein!")
        
    # def clean_vorname(self):
    #     data = super(KundeForm, self).clean()
    #     print(data.get('vorname'))
    #     if 'halder' in data.get('vorname'):
    #         print("Test False----------------- ")
    #         self.add_error('vorname', "passwords do not match !")
    #         raise forms.ValidationError("Test False----------------- ")
    #     return data
    
    # def save(self, commit=True):
    #     instance = super(KundeForm, self).save(commit=False)
    #     instance.vorname = self.vorname
    #     instance.nachname = self.nachname
    #     instance.benutzer_name = self.benutzer_name
    #     instance.email_add = self.email_add
    #     instance.pswd = self.pswd
    #     if commit:
    #         instance.save()
    #     return instance

class GeheimFAForm(forms.ModelForm):
    geheime_frage = forms.CharField(label='Geheime Frage', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    geheime_antwort = forms.CharField(label='Geheime Antwort', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = GeheimeFA
        fields = ['geheime_frage', 'geheime_antwort']

class LoginForm(forms.Form):
    benutzer_name = forms.CharField(max_length=200, label='Benutzername', widget=forms.TextInput(attrs={'class': 'form-control'}))
    pswd = forms.CharField(label='Kennwort',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # def __init__(self, request=None, *args, **kwargs):
    #     self.request = request
    #     self.kunde = None
    #     super().__init__(*args, **kwargs)
    # def clean(self):
    #     benutzer_name = self.cleaned_data.get('benutzer_name')
    #     pswd = self.cleaned_data.get('pswd')
    #     if benutzer_name is not None and pswd:
    #         self.kunde = authenticate(self.request, benutzer_name=benutzer_name, pswd=pswd)
    #         if self.kunde is None:
    #             print("No entry!--------------------------")
    #         print(self.kunde.vorname)
    #     return self.cleaned_data

    def clean_benutzer_name(self):
        benutzerName = self.cleaned_data.get('benutzer_name')
        try:
            kunde = Kunde.objects.get(benutzer_name=benutzerName)
            print(kunde.vorname)
        except:
            print("No entry!--------------------------")        