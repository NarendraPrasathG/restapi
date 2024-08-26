from django.urls import path
from .views import ProductView, ProductViewID

urlpatterns = [
    path('products/', ProductView.as_view(), name='product-list'),
    path('products/<int:id>/', ProductViewID.as_view(), name='product-detail'),
]
