from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField


class Category(models.Model):
    name = models.CharField(max_length=100)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    thumbnails = ImageSpecField(source='image', processors=[ResizeToFill(150,150)], format="PNG", options={'quality':90})
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

