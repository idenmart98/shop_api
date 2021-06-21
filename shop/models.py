from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)


class Product(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

