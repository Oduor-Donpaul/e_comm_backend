from django.shortcuts import render
from .models import Product, Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer, CategorySErializer

@api_view(['GET'])
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    category_serializer = CategorySErializer(categories, many=True)
    product_serializer = ProductSerializer(products, many=True)

    data = {
        "categories":category_serializer.data,
        "products":product_serializer.data,
    }

    return Response(data)
  

@api_view(['GET'])
def product_datail(request, product_id):
    try:
       product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
       return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
   
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)