from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('progress', 'In Progress'),
    ('fineshed', 'Fineshed'),
    ('paid', 'Paid'),
    ('delivered', 'Delivered'),
)

CONTACT_ME_CHOICES = (
    ('sent', 'Sent'),
    ('checked', 'Checked')
)


class Catagory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Catagories'

    def __str__(self):
        return self.name


class Product(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='uploads')

    def __str__(self):
        return self.name

    # def get_name(self):
    #     return self.name

class ProductCounter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name
    

class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    product_counter = models.ForeignKey(ProductCounter, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    #products = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    is_done = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    

    def __str__(self):
        return self.client.username
        
class Cart(models.Model):
    headline = models.CharField(max_length=100)
    order = models.ManyToManyField(Order)   
    status = models.CharField(max_length=20,
        choices=ORDER_STATUS_CHOICES, default='created')

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
    

# The model for "Contact" me form
class ContactMe(models.Model):
    # User's email
    user_email = models.EmailField()
    # title
    message_title = models.CharField(max_length=70)
    # message
    message = models.TextField()
    # when the message arrived (is saved in the db)
    created_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=20,
        choices=CONTACT_ME_CHOICES, default='sent')

class ProductInformation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads')