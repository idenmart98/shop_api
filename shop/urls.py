from shop.serializers import ProductListSerializer
from django.urls import path
from .views import ProductListView, CategoryListView, ProductRetrevieUpdateDeleteView, ProductCreateView, CategoryRetrieveUpdateDeleteView


urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view()),
    path('add_product/', ProductCreateView.as_view())

]

