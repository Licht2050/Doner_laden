
from django.shortcuts import render, redirect
from .forms import RegistrationsForm, LoginForm, ContactMeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
#from django.core.exceptions import ValidationError
from django import forms

from django.core.mail import send_mail

# Create your views here.

# def registerUser(request):
    
#     if request.method == "POST":
#         loginForm = LoginForm(request.POST, request)
#         form = RegistrationsForm(request.POST)
#         if 'registration' in request.POST:
#             if form.is_valid():
#                 form.save()
#                 return redirect("home")
#         if loginForm.is_valid():
#             print("Login Form vor pruefen No entry!--------------------------")
#             loginValid(request)
#             print("Login Form nach pruefen No entry!--------------------------")
        
        
#     else:
#         form = RegistrationsForm()
#         loginForm = LoginForm()
#     return render(request, 'benutzerSicht/html_modals/registration_modal.html',{'regForm':form, 'loginForm': loginForm})

def home(request):
    
    if request.method == "POST":
        contact_me_form = ContactMeForm(request.POST)
        
        email = request.POST.get('user_email')
        title = request.POST.get('message_title')
        message = request.POST.get('message')

        if "contact_me_form" in request.POST:
            if contact_me_form.is_valid():
                contact_me_form.save()

                # send_mail(
                #     "title,
                #     message,
                #     email,
                #     ['geokehaiov@gmail.com'],
                #     fail_silently=False,
                # )
                
                return redirect("home")

    contactMeForm = ContactMeForm()

    return render(request, 'benutzerSicht/index.html', {'ContactMeForm':contactMeForm})

def loginUser(request):
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        uname = request.POST.get('username')
        pwd = request.POST.get('pswd')
        if loginform.is_valid():
            if uname is not None and pwd:
                user = authenticate(request ,username=uname, password=pwd)
                if user is not None:
                    login(request, user)
                    return render(request, 'benutzerSicht/index.html',{'user':user})
                else:
                    print("Login failed!")
                    #raise forms.ValidationError("Login Faild!")
    else:
        loginform = LoginForm()
    return render(request, 'benutzerSicht/login.html',{'loginForm':loginform})

def registerUser(request):
    
    if request.method == "POST":
        form = RegistrationsForm(request.POST)
        if 'registration' in request.POST:
            if form.is_valid():
                form.save()
                return redirect("home")
        
    else:
        form = RegistrationsForm()
        
    return render(request, 'benutzerSicht/registration.html',{'regForm':form})

# def logoutUser(request):
