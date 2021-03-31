from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, ContactMe, Order, ProductCounter



class RegistrationsForm(UserCreationForm): 
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


    #Es wird nach email in der Datenbank geprueft. Falls vorhaden ist, wird Error ausgeworfen.
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            user_email = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Username {email} ist schon vorhanden!")

    #Falls Benutzername schon registriert ist wird Error ausgeworfen.
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

    #Wird nach username und password ueberprueft. Falls nicht stimmt wird Error ausgeworfen.
    def clean(self):
        if self.is_valid():
            uname = self.cleaned_data['username']
            pwd = self.cleaned_data['password']
            if uname is not None and pwd:
                if not authenticate(username=uname, password=pwd):
                    raise forms.ValidationError("Invalid Login")
 
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

class ProductCounterForm(forms.ModelForm):

    class Meta:
        model = ProductCounter
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})


    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        #Falls Quantity < 0 wird Error ausgeworfen.
        if quantity is not None and quantity > 0:
            return cleaned_data
        raise forms.ValidationError('Quantity should be > 0!')


class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = [ 'description']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'form-control'})

