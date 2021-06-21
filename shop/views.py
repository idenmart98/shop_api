from shop.models import Product, Category
from django.shortcuts import render
from .serializers import ProductListSerializer, CategoryListSerializer
from rest_framework import generics
# Create your views here.


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer



