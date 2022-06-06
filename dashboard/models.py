from django.db import models

# Create your models here.
class ad_profile(models.Model):
    img=models.ImageField(null=True)
    name=models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.IntegerField(null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    address=models.TextField(blank=True,null=True)
    def __str__(self) -> str:
        return self.name   

class frgt_pwd(models.Model):
   
    frg_token=models.CharField(max_length=1000)
    def __str__(self):
        return self.user.username          