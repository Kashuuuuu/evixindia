from operator import mod
from django.db import models

# Create your models here.

class be_dealer(models.Model):
    name = models.CharField(max_length=500)
    mobile = models.IntegerField()
    email = models.CharField(max_length=500)
    website = models.CharField(max_length=500)
    organisation = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    firm = models.CharField(max_length=500)
    gst = models.CharField(max_length=500)
    account = models.IntegerField(max_length=500)
    ifsc = models.CharField(max_length=500)
    accountholder = models.CharField(max_length=500)
