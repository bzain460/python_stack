from django.db import models
import re

class userManager(models.Manager):
    def reg(self, postData):
        errors = {}
        if postData['first_name'].isalpha()!= True:
            errors["first_name"] = "first name should be only characters"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first name should be at least 2 characters"
        if postData['last_name'].isalpha()!= True:
            errors["last_name"] = "last name should be only characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last name should be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = "Invalid email address!"

        if len(postData['pass']) < 8:
            errors["pass"] = "password should be at least 8 characters"

        if postData['pass'] != postData['cpass']:
            errors["pass"] = "password should match password confirmation"
        return errors

    def log(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['Lemail']):         
            errors['Lemail'] = "Invalid email address!"

        if len(postData['Lpass']) < 8:
            errors["Lpass"] = "password should be at least 8 characters"
        return errors

    def new(self, postData):
        errors = {}

        if len(postData['thought']) < 5:
            errors["thought"] = "thoughts should be at least 5 characters"
        return errors

class user(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

class thought(models.Model):
    thought = models.TextField(null = True)
    users = models.ManyToManyField(user, related_name="thoughts")
    posted_by = models.ForeignKey(user, related_name="posted_thoughts", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()