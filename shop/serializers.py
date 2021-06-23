from rest_framework import fields, serializers
from .models import Product, Category


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['created', 'is_active']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

<<<<<<< HEAD

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

=======
class ProductCreateSerializator(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
>>>>>>> 397507b4831a97bdfec98a0d9faf3a16ddbaf3e7
