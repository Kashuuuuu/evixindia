from statistics import mode
from django.db import models

# Create your models here.
class products(models.Model):
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)
  
    product_name = models.CharField(max_length=1000)
    time = models.CharField(max_length=500)
    s1 = models.CharField(max_length=500)
    s2 = models.CharField(max_length=500)
    speed = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)

