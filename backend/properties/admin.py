from django.contrib import admin
from .models import Owner, Property, Category

admin.site.register(Owner)
admin.site.register(Category)
admin.site.register(Property)

