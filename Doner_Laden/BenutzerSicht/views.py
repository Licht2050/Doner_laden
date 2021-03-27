
from django.shortcuts import render, redirect
from .forms import RegistrationsForm, LoginForm, ContactMeForm, OrderForm, ProductCounterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
#from django.core.exceptions import ValidationError
from django import forms
from .models import Product, Catagory, Order, ProductCounter

from django.core.mail import send_mail

# Create your views here.


def home(request):
    products = Product.objects.all()

    orderForm = OrderForm(request.POST)
    prdCounterForm = ProductCounterForm(request.POST)
    order = Order.objects.all()

    for ord in order:
        print(ord.client.first_name)
    
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

    return render(request, 'benutzerSicht/index.html', {'ContactMeForm':contactMeForm, 'products':products, 'orderForm':orderForm, 'prdCounterForm': prdCounterForm})
    # return render(request, 'benutzerSicht/index.html', {'doner':doner})

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

# def OrderView(request):

#     orderForm = OrderForm(request.POST)
    
#     return render(request, 'benutzerSicht/product_list_price.html',{'product':product})
    
