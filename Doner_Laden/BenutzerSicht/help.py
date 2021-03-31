
from MitarbeiterSicht.models import ResourceProduct
from django.db.models import F


KEBAB = {
    'tomato'        : 3,
    'bread'         : 2,
    'onien'         : 4,
    'doner_meat'     : 5
}

PIZZA = {
    'pizza_dough'    : 1,
    'tomato_sauce'   : 2,
    'onien'         : 2,
    'tomato'        : 2,
    'salami_pack'    : 1,
    'cheese'        : 1
}



#Nach jede Bestellung wird auch Resource Producten substrahiert.
def ResourcenCalculation(productSlug, productCatagory , quantity):
    
    if productCatagory == 'Kebab':
        for key in KEBAB:
            ResourceProduct.objects.filter(slug=key).update(quantity=F('quantity') - (quantity * KEBAB[key]))

    if productCatagory == 'Pizza':
        for key in PIZZA:
            ResourceProduct.objects.filter(slug=key).update(quantity=F('quantity') - (quantity * KEBAB[key]))
    
    if productCatagory == 'Drinks':
        ResourceProduct.objects.filter(slug=productSlug).update(quantity=F('quantity') - quantity)
