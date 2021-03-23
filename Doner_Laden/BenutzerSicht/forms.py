from django.core.exceptions import ValidationError
from django import forms
from .models import Kunde



class KundeForm(forms.Form):
    vorname = forms.CharField(max_length=200, label='Vorname', widget=forms.TextInput(attrs={'class': 'form-control'}))
    nachname = forms.CharField(max_length=200, label='Nachname', widget=forms.TextInput(attrs={'class': 'form-control'}))  
    benutzer_name = forms.CharField(max_length=200, label='Benutzername', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email_add = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    pswd = forms.CharField(label='Kennwort',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    pswd_wdh = forms.CharField(label='Wiederhole Kennwort', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    gehim_frage = forms.CharField(label='Geheime Frage', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gehim_answer = forms.CharField(label='Geheime Antwort', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #password felder mit einander vergleichen.
    # def clean(self):
    #     valpswd = self.cleaned_data['pswd']
    #     valpswd_wdh = self.cleaned_data['pswd_wdh']
    #     if valpswd != valpswd_wdh:
    #         raise forms.ValidationError('kennwort stimmen nicht ueberein!')

    # class Meta:
    #     model = Kunde
    #     fields = ['vorname', 'nachname', 'benutzer_name', 'email_add', 'pswd', 'geheimeFA']
    
    # def clean_pswd(self):
    #     pswd = self.cleaned_data.get('pswd')
    #     if len(pswd) < 8:
    #         #self.errors['pswd'] = self.error_class(['kennwort stimmen nicht ueberein!'])
    #         raise forms.ValidationError("kennwort stimmen nicht ueberein!") 
    #     return pswd

    def clean_vorname(self):
        data = super(KundeForm, self).clean()
        print(data.get('vorname'))
        if 'halder' in data.get('vorname'):
            print("Test False----------------- ")
            self.add_error('vorname', "passwords do not match !")
            raise forms.ValidationError("Test False----------------- ")
        return data

