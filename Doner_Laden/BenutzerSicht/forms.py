from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationsForm(UserCreationForm): 
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
    def clean_username(self):
       uname = self.cleaned_data.get('username')
       if uname == 'henri':
           raise ValidationError("Fehler beim Username")     

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, label='Benutzername', widget=forms.TextInput(attrs={'class': 'form-control'}))
    pswd = forms.CharField(label='Kennwort',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # def clean(self, request):
    #     uname = self.cleaned_data.get('username')
    #     pwd = self.cleaned_data.get('pswd')
    #     print("No entry!--------------------------")
    #     #if uname is not None and pwd:
    #     user = authenticate(request ,username=uname, password1=pwd)
    #     if user is None:
    #         print("No entry!--------------------------")
    #     print("No entry!--------------------------")
    #     print(user.name)
    #     return self.cleaned_data
    