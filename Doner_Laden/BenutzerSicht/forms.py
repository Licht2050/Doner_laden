from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactMe


class RegistrationsForm(UserCreationForm): 
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            user_email = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Username {email} ist schon vorhanden!")

    def clean_username(self):
        uname = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=uname)
        except Exception as e:
            return uname
        raise forms.ValidationError(f"Username {uname} ist schon vorhanden!")

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'password']

    # def clean(self):
    #     uname = self.cleaned_data.get('username')
    #     pwd = self.cleaned_data.get('pswd')
    #     print("Vor If !--------------------------")
    #     #if uname is not None and pwd:
    #     if uname is not None and pwd:
    #             user = authenticate(request ,username=uname, password=pwd)
    #             if user is not None:
    #                 login(request, user)
    #                 return render(request, 'benutzerSicht/index.html',{'user':user})
    #             else:
    #                 print("Login failed!")
    #                 raise  forms.ValidationError("Login Vaild")
    #     return self.cleaned_data
    
class ContactMeForm(forms.ModelForm):

    class Meta:
        model = ContactMe
        fields = ['user_email', 'message_title', "message"]

    # User's email
    user_email = forms.EmailField(label='Email')
    # title
    message_title = forms.CharField(label='Title', max_length=70)
    # message
    message = forms.Textarea()

