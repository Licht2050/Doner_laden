
from django.shortcuts import render, redirect
from .forms import RegistrationsForm, LoginForm, ContactMeForm, OrderForm, ProductCounterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
#from django.core.exceptions import ValidationError
from django import forms
from .models import Product, Catagory, Order, ProductCounter, Cart, ProductInformation
from django.views.generic import TemplateView
from .help import ResourcenCalculation


from django.core.mail import send_mail

# Create your views here.

#Die globale Variablen wird bei Hinzufuegen in der Einkaufswagen bentuzt.
#Nach der Erfolgreische Bestellung wird wieder mit "0" initialisiert
orderListe = []
productQuantityListe = [0]
totalPriceListe = [0.0]


#In  Index wird folgende Argumente uebergeben:
#@ProductInformation
#@ContactMeForm
#@Product
#@OrderForm
#@ProductCounterForm
#@orderListe
#@productQuantityListe
#@totalPriceListe
#@totalPriceListe
class HomeView(TemplateView):
    template_name = 'benutzerSicht/index.html'
    

    def get(self, request):
        context1 = {}
        context1['productInformation'] = ProductInformation.objects.all()
        context1['ContactMeForm'] = ContactMeForm()
        context1['products'] = Product.objects.all()
        context1['catagories'] = catagory = Catagory.objects.all()
        context1['orderForm'] = OrderForm()
        context1['prdCounterForm'] = ProductCounterForm()
        context1['bestellung'] = orderListe
        context1['productAnzahl'] = productQuantityListe[0]
        context1['product_total_price'] = totalPriceListe[0]

        return render(request, self.template_name, context1)

    def post(self, request):
        context = {}
        context['ContactMeForm'] = ContactMeForm(request.POST)
        context['orderForm'] = OrderForm(request.POST)
        context['prdCounterForm'] = ProductCounterForm(request.POST)

        #Hier werden die Produkte in der Einkaufswagen hinzugefuegt.
        if "addToCart" in request.POST:
            if context['prdCounterForm'].is_valid():
                productID = int(request.POST.get("addToCart"))
                quanity = int(context['prdCounterForm'].cleaned_data['quantity'])
                description = request.POST.get('description')
                
                product = Product.objects.get(id=productID)
                
                #Falls der Einkaufswagen leer ist, wird ein neues ProductCounter Object und
                #Order object erstellt.
                if not orderListe:
                    
                    product_Counter = ProductCounter(product=product, quantity=quanity)
                    order = Order(description=description, product_counter=product_Counter)
                    orderListe.append(order)

                #Wenn Produkte schon in der Einkaufswagen Hinzugefuegt ist, wird 
                # in diesem Schritt ueberprueft, ob das Produkt ebenso in der Wagen hinzugefuegt ist
                # Falls ja wird nur der Anzahl des Produktes erhoeht, Falls nein wird ein neues Object erstellt. 
                else:
                    for ord in orderListe:
                        if ord.product_counter.product == product:
                            ord.product_counter.quantity += quanity
                            productQuantityListe[0] += quanity
                            totalPriceListe[0] +=(quanity* product.price)
                            return redirect('home')

                    product_Counter = ProductCounter(product=product, quantity=quanity)
                    order = Order(description=description, product_counter=product_Counter)
                    orderListe.append(order)
                    
                productQuantityListe[0] += quanity
                totalPriceListe[0] += (quanity* product.price)  
                return redirect('home')
        
        #Sobald der Kunde auf die bestellung Button drueckt, wird in der Template ueberprueft,
        #ob der Kunde schon eingelogt ist.
        #Falls er nicht eingelogt ist, wird zu Sign In weitergeleitet.
        #Falls er eingelogt ist, wird hier nach dieser If-Bedingung seine Bestellung in der Datenbank
        #erfolgreich gespeichert. und die golobale Variablen ebenso mit "0" initialisiert.
        if "order_summery" in request.POST:
            cart = Cart(headline=request.user)
            cart.save()
            for order in orderListe: 
                order.product_counter.save()
                productSlug =order.product_counter.product.slug
                productCatagory = order.product_counter.product.catagory.name
                productQuantity = order.product_counter.quantity
                ResourcenCalculation(productSlug, productCatagory, productQuantity)

                order.client = request.user
                order.save()
                cart.order.add(order)
            orderListe.clear()
            productQuantityListe[0] = 0
            totalPriceListe[0] = 0.0
            return redirect('home')
        
        
        contact_me_form = ContactMeForm(request.POST)
        
        
        #Wenn der Kunde dem Geschaeft kontaktieren moechte kann er in dem Template 
        #seine Nachricht eingeben. und nach Korrecte eingabe wird seine Nachricht in der Datenbank
        #gespeichert. Alle Nachrichten die noch nicht von den Mitarbeitern gelesen sind, wird in der MitarbeiterSicht angezeigt.
        if "contact_me_form" in request.POST:
            if context['ContactMeForm'].is_valid():
                context['ContactMeForm'].save()

                return redirect("home")
        
        if "update" in request.POST:
            return redirect('home')

        context['productAnzahl'] = productQuantityListe[0]
        context['product_total_price'] = totalPriceListe[0]
        
        return render(request, self.template_name, context)

def RemoveFromCard(self, id):

    if orderListe is not None:
        for o in orderListe:
            if o.product_counter.product.id == id:
                productQuantityListe[0] -= o.product_counter.quantity
                totalPriceListe[0] -= (o.product_counter.quantity * o.product_counter.product.price)
                orderListe.remove(o)

    return redirect('home')

#Bei Sign Out wird folgende Funktion aufgerufen.
def logoutUser(request):
    logout(request)
    return redirect("home")
    
#folgende Parameter wird in login Template uebergeben:
# @   LoginForm
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


#folgende Parameter wird in register Template uebergeben:
# @   RegistrationsForm
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

