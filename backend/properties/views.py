from django.shortcuts import render
from .serializer import CategorySerializer, OwnerSerializer, PropertySerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Owner, Category, Property

@api_view(['GET'])
def owner_details(request, owner_id):
    try:
        details = Owner.objects.get(pk=owner_id)

    except Owner.DoesNotExist:
        return Response({"error":"user not found"}, status=status.HTTP_404_NOT_FOUND)

    details_serializer = OwnerSerializer(details)

    return Response(details_serializer.data)

@api_view(['GET'])
def property_details(request, property_id):
    try:
        the_property = Property.objects.get(pk=property_id)
    
    except Property.DoesNotExist:

        return Response({"error":"property does not exist"})

    property_serializer = PropertySerializer(the_property)

    return Response(property_serializer.data)

@api_view(['GET'])
def property_page_view(request):

    properties = Property.objects.all()
    categories = Category.objects.all()

    properties_serializer = PropertySerializer(properties, many=True)
    categories_serializer = CategorySerializer(categories, many=True)

    data = {
        "categories":categories_serializer.data,
        "properties":properties_serializer.data,
    }

    return Response(data)