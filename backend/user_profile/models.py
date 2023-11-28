from django.db import models
from accounts.models import CustomUser

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(default='')
    first_name = models.CharField(max_length=30, default='first_name')
    last_name = models.CharField(max_length=30, default='last_name')
    description = models.CharField(max_length=200, default='description')
    phone_number = models.CharField(max_length=13, blank=True, null=True)

class ShippingAdress(models.Model):
    first_name = models.CharField(max_length=30, null=False, default='user_name')
    last_name = models.CharField(max_length=30, null=False, default='user_name')
    delivery_adress = models.CharField(max_length=30)
    town = models.CharField(max_length=30)
    pickup_station = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)