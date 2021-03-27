from django.db import models

# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    
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
    image = models.ImageField(upload_to='uploads')
    quantity = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.name

    
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
