from django.db import models

# Create your models here.
class Customer(models.Model):
    # primary key for customer table - autoincrements
    customerId = models.AutoField(primary_key=True) 
    firstName = models.CharField(max_length=50,unique=False)
    lastName = models.CharField(max_length=70,unique=False)
    password = models.CharField(max_length=50,unique=False)
    email = models.EmailField(max_length=254,unique=True)
    githubUserName = models.CharField(max_length=254,null=True)
    activity = models.CharField(null=True,max_length=254)
    