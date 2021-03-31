from django import template

register = template.Library()


@register.filter
def modulo(num, val):
    return num % val == 1
    
@register.filter
def in_category(resourceProduct, catagory):
    return resourceProduct.filter(catagory=catagory)
