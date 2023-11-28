from django.shortcuts import render
from .models import Blog, Category
from .serializer import BlogSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def blog_page(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()

    category_serializer = CategorySerializer(categories, many=True)
    blog_serializer = BlogSerializer(blogs, many=True)

    data = {
        "blogs":blog_serializer.data,
        "categories":category_serializer.data,
    }

    return Response(data)

@api_view(['GET'])
def blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return Response({"error":"blog not found"}, status=status.HTTP_404_NOT_FOUND)
    blog_serializer = BlogSerializer(blog)

    return Response(blog_serializer.data, status=status.HTTP_200_OK)

