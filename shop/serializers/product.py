from rest_framework import fields, serializers
from shop.models import Product

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['created', 'is_active']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializator(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


