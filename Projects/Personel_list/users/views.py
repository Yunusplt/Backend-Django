from django.shortcuts import render
from .serializers import ProfileSerializer,Profile, UserSerializer, User
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class ProfileMVS(ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class = ProfileSerializer

class UserMVS(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer