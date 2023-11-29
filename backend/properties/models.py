from django.db import models
from imagekit.models import ImageSpecField
from imagekit .processors import ResizeToFill

class Owner(models.Model):
    image = models.ImageField(upload_to='profile_images/', default='default.png')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    reviews = models.IntegerField()

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Property(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/', default='default.png')
    thumbnail = ImageSpecField(source=image, processors=[ResizeToFill(150,150)], format="PNG", options={'quality':90})
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    discount = models.DecimalField(max_digits=15, decimal_places=2)
    address = models.CharField(max_length=255)
    bedrooms =  models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    parking_capacity = models.PositiveIntegerField()
    features = models.JSONField()
