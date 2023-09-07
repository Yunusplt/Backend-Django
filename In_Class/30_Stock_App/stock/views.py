from django.shortcuts import render
from rest_framework.permissions import IsAdminUser,DjangoModelPermissions

from .serializers import (
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
    FirmSerializer,
    PurchasesSerializer,
    SalesSerializer,
    Category,
    Brand,
    Product,
    Firm,
    Purchases,
    Sales,
    
)
# Create your views here.
from rest_framework.viewsets import ModelViewSet


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAdminUser]
    permission_classes = [DjangoModelPermissions]