from rest_framework import serializers
from .models import Owner, Category, Property

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class PropertySerializer(serializers.ModelSerializer):

    category = CategorySerializer()

    class Meta:
        model = Property
        fields = ['id', 'category', 'name', 'description', 'price', 'discount', 'address', 'bedrooms', 'bathrooms', 'size', 'parking_capacity', 'features']

