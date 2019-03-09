from django.db import models

from customer.models import Customer
from rest_framework import serializers

# Create your models here.
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customerId','firstName','lastName','password','email')
