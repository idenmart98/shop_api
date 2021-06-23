from shop.serializers import ProductListSerializer
from django.urls import path
<<<<<<< HEAD
from .views import ProductListView, CategoryListView, ProductRetrieveUpdateDeleteView, CategoryRetrieveUpdateDeleteView
=======
from .views import ProductListView, CategoryListView, ProductRetrevieUpdateDeleteView, ProductCreateView
>>>>>>> 397507b4831a97bdfec98a0d9faf3a16ddbaf3e7


urlpatterns = [
    path('products/', ProductListView.as_view()),
<<<<<<< HEAD
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view()),
=======
    path('products/<int:pk>/', ProductRetrevieUpdateDeleteView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('add_product/', ProductCreateView.as_view())
>>>>>>> 397507b4831a97bdfec98a0d9faf3a16ddbaf3e7
]
