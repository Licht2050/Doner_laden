from django.db import models

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