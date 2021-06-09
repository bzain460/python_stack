from django.db import models

# Create your models here.
class Dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField (auto_now=True)                                                             



class Ninja(models.Model):
    First_name=models.CharField(max_length=255)
    Last_name=models.CharField(max_length=255) 
    dojo=models.ForeignKey(Dojo,related_name='ninjas',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField (auto_now=True)                                                             
