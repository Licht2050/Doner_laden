from __future__ import unicode_literals
 
from django.contrib import admin
from .models import ResourceCatagory, ResourceProduct

admin.site.register(ResourceProduct)
admin.site.register(ResourceCatagory)