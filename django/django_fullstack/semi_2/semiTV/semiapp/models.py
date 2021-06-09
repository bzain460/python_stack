from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['title']) < 2:
            errors["Title"] = "Show Title should be at least 5 characters"
        if len(postData['net']) < 3:
            errors["Network"] = "The Network name should be at least 5 characters"
        if len(postData['desc']) > 0 and len(postData['desc'])< 10:
            errors["desc"] = "Show description should be at least 10 characters, You can leave it empty if you don't want to add one"
        return errors





class TV(models.Model):
    Title=models.CharField(max_length=255)
    Network=models.CharField(max_length=255)
    Release_date= models.DateField()
    Description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = ShowManager()

def add_show(Title,Network,Release_date,Description):
    return TV.objects.create(Title=Title,Network=Network,Release_date=Release_date,Description=Description)


