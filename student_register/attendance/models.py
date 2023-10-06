from django.db import models


class Student(models.Model):
    name = models.CharField(blank=False, max_length=100)
    email_address = models.CharField(blank=False, max_length=100) 
    phone = models.IntegerField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(blank=False)
    address = models.CharField(blank=False, max_length=100)
    course = models.CharField(blank=False, max_length=100)
    

class Register(models.Model):
    name = models.CharField(blank=False, max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    attendance = models.CharField(max_length=100, blank=False)

       

 



# Create your models here.
