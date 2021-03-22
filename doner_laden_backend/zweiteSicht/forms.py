from django.core import validators
from django import forms

class KundeForm(forms.Form):
    vorname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nachname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))  
    benutzer_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email_add = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    pswd = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    pswd_wdh = forms.CharField(label='Password wiederholen', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    gehim_frage = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gehim_answer = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #password felder mit einander vergleichen.
    def clean(self):
        cleaned_data = super().clean()
        valpswd = self.cleaned_data['pswd']
        valpswd_wdh = self.cleaned_data['pswd_wdh']
        if valpswd != valpswd_wdh:
            raise forms.ValidationError('kennwort stimmen nicht ueberein!')

    
