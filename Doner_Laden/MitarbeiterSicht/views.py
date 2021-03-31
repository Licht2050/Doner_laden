from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from json import dumps
from BenutzerSicht.models import Product, Order, ContactMe, Cart, Order
import datetime
from .forms import ResourceProductForm
from .models import ResourceProduct, ResourceCatagory
from django.db.models import F


#Folgenden Parametern wird in Mitarbeiter("index.html") Template uebergeben:
# @ ContactMe
@login_required(login_url='homeMitarbeiterSicht')
def staffView(request):
    # get all messages from client's contact me
    all_messages = ContactMe.objects.filter(status='sent')

    if request.method == "POST":
        message_id = request.POST.get('message_id')

        if "message_done" in request.POST:
            # change the status of the message to true for read

            ContactMe.objects.filter(id=message_id).update(status='checked')

        if "message_delete" in request.POST:
            # delete the message
            message = ContactMe.objects.filter(id=message_id).delete()

    context_to_render = {
        "all_messages"          : all_messages,
    }

    return render(request, 'index.html', context_to_render)


# Folgenden Parametern wird in Rosource Templates uebergeben:
# @ ResourceProductForm
# @ resourceProduct
# @ resourceCatagory
# @ ResourceProductForm
def Resources(request):
    context = {}
    template_name = 'resources.html'

    # get the  resource lists from dthe db
    resourceProduct = ResourceProduct.objects.all()
    resourceCatagory = ResourceCatagory.objects.all()

    # objects to context
    context['productQuantity'] = ResourceProductForm()
    context['resourceProduct'] = resourceProduct
    context['resourceCatagory'] = resourceCatagory
    context['resourceForm'] = ResourceProductForm()

    if request.method == "POST":
        context['resourceForm'] = ResourceProductForm(request.POST)
        ResourceProduct.objects.filter(id=request.POST.get('name')).update(quantity=F('quantity')+request.POST.get('quantity'))
 
    return render(request, template_name, context)

def Messages(request):
    # get all messages from client's contact me
    all_messages = ContactMe.objects.filter(status='sent')

    if request.method == "POST":
        message_id = request.POST.get('message_id')

        # delete and change status of the messages
        if "message_done" in request.POST:
            """ change the status of the message to true for read"""
            ContactMe.objects.filter(id=message_id).update(status='checked')

        if "message_delete" in request.POST:
            # delete the message
            message = ContactMe.objects.filter(id=message_id).delete()
            
    context_to_render = {
        "all_messages"          : all_messages,
    }

    return render(request, 'messages.html', context_to_render )

def Orders(request):
    context = {}
    # get the cart objects with status created from db
    cartTest = Cart.objects.filter(status='created')

    # after done is pressed change the status of each order to fineshed
    if request.method == "POST":
        if "order_done" in request.POST:
            cartId = request.POST.get('order_done')
            Cart.objects.filter(id=cartId).update(status='fineshed')

    context['cart'] = cartTest
    return render(request, 'orders.html', context )

def Statistic(request):
    # get the statistics
    dates_set = set()

    statistic_labels = []
    statistic_counter_kebab = []
    statistic_counter_pizza = []
    statistic_counter_drinks = []

    # get all orders stored in the db
    all_orders = Order.objects.all()

    # get the set of all order_dates existing in the db
    for order in all_orders:
        date_to_use = datetime.date(order.order_date.year, order.order_date.month, order.order_date.day)
        dates_set.add(date_to_use)

    # first the set should be converted to a list and sorted!!!
    sorted_date_list = []
    for date in dates_set:
        sorted_date_list.append(date)

    # sort it
    sorted_date_list.sort()

    for date_to_use in sorted_date_list:
        # search for every order in the db with a date from the order's set
        orders = Order.objects.filter(order_date__date=datetime.date(date_to_use.year, date_to_use.month, date_to_use.day))

        # change the format of the date
        date_to_string = date_to_use.strftime("%d-%m-%Y")
        statistic_labels.append(date_to_string)
        
        kebab_counter = 0
        pizza_counter = 0
        drinks_counter = 0

        for order in orders:
            # for each order for each date get the category
            category = order.product_counter.product.catagory.name

            # separate in the variables
            if category == "Kebab":
                kebab_counter += order.product_counter.quantity
            if category == "Pizza":
                pizza_counter += order.product_counter.quantity
            if category == "Drinks":
                drinks_counter += order.product_counter.quantity

        # safe in the lists -> example: for 2021-03-27 we have 0 Kebab, 14 Pizza and 0 drinks sold (ordered)
        statistic_counter_kebab.append(kebab_counter)
        statistic_counter_pizza.append(pizza_counter)
        statistic_counter_drinks.append(drinks_counter)

    # sort the date labels    
    statistic_labels.sort()

    context_to_render = {
        "statistic_label_data"  : dumps(statistic_labels),
        "statistic_kebab_data"  : statistic_counter_kebab,
        "statistic_pizza_data"  : statistic_counter_pizza,
        "statistic_drinks_data" : statistic_counter_drinks,
    }

    return render(request, 'statistics.html', context_to_render)