from shop.models import Product, Category
from django.shortcuts import render
<<<<<<< HEAD
from .serializers import ProductListSerializer, CategoryListSerializer, ProductDetailSerializer, CategoryDetailSerializer
=======
from .serializers import ProductListSerializer, CategoryListSerializer, ProductDetailSerializer, ProductCreateSerializator
>>>>>>> 397507b4831a97bdfec98a0d9faf3a16ddbaf3e7
from rest_framework import generics
# Create your views here.


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class ProductCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializator
    # permission_classes = Product.seller


class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

