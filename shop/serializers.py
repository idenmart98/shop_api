from rest_framework import serializers
from .models import Product, Category

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['created', 'is_active']

