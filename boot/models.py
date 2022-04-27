import email
from email import message
from ssl import create_default_context
from django.db import models

# Create your models here.

class Inquiry(models.Model):
    fullname = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    message = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



   
