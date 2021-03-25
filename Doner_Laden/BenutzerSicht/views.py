from django.shortcuts import render, redirect
from .forms import RegistrationsForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def loginValid(request):
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        uname = request.POST.get('username')
        pwd = request.POST.get('pswd')
        if loginform.is_valid():
            if uname is not None and pwd:
                user = authenticate(request ,username=uname, password=pwd)
                if user is not None:
                    login(request, user)
                    redirect("home")
                else:
                    print("Login failed!")
    else:
        loginform = LoginForm()
    return render(request, 'benutzerSicht/html_modals/login_modal.html',{'loginForm':loginform})

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

def regTest(request):
    
    if request.method == "POST":
        form = RegistrationsForm(request.POST)
        if 'registration' in request.POST:
            if form.is_valid():
                form.save()
                return redirect("home")
        
    else:
        form = RegistrationsForm()
        
    return render(request, 'benutzerSicht/html_modals/registration_modal.html',{'regForm':form})

def home(request):
    return render(request, 'benutzerSicht/home.html')