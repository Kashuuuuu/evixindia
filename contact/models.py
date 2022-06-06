from operator import mod
from django.db import models

# Create your models here.
class contactus(models.Model):
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    mobile = models.IntegerField()
    service = models.CharField(max_length=500)
    enquiry = models.TextField(max_length=1000)

