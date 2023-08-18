from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import Personel,PersonelSerializer,Department,DepartmentSerializer

# Create your views here.


class PersonelMVS(ModelViewSet):
    queryset=Personel.objects.all()
    serializer_class=PersonelSerializer

class DepartureMVS(ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer

