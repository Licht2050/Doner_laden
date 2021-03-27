
from django.shortcuts import render, redirect
from .forms import RegistrationsForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
#from django.core.exceptions import ValidationError
from django import forms
from .models import Product, Catagory

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
    doner = Product.objects.get(name="XXL Doner")
    
    print(doner.catagory.description) 
    return render(request, 'benutzerSicht/index.html', {'doner':doner})

def logoutUser(request):
    logout(request)
    return redirect("home")

def loginUser(request):
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            uname = request.POST.get('username')
            pwd = request.POST.get('password')
            if uname is not None and pwd:
                user = authenticate(username=uname, password=pwd)
                if user is not None:
                    login(request, user)
                    return redirect("home")
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

def ProductView_as_Catagories(request):
    
    product = Catagory.objects.get(name="XXL Doner")
    print(product.price) 
    return render(request, 'benutzerSicht/product_list_price.html',{'product':product})
    
