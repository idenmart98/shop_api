from shop.serializers import ProductListSerializer
from django.urls import path
from .views import ProductListView, CategoryListView, ProductRetrevieUpdateDeleteView


urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductRetrevieUpdateDeleteView.as_view()),
    path('categories/', CategoryListView.as_view())
]