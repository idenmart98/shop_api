from shop.models import Product
from django.shortcuts import render
from .serializers import ProductListSerializer
from rest_framework import generics
# Create your views here.


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer