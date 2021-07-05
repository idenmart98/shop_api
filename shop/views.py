from shop.models import Product, Category
from authead.models import BaseUserManager
from django.shortcuts import render
from .serializers import ProductListSerializer, CategoryListSerializer, ProductDetailSerializer, \
    CategoryDetailSerializer, ProductCreateSerializator, CategoryCreateSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import generics


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


class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CategoryCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser,]
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer

