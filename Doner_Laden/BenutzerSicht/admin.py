from django.contrib import admin
from .models import Product, Catagory, Order,  ContactMe, ProductCounter

# Register your models here.

admin.site.register(Product)
admin.site.register(Catagory)
admin.site.register(Order)
admin.site.register(ContactMe)
admin.site.register(ProductCounter)