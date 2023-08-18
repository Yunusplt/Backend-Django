from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Category,
    CategorySerializer, 
    Post,                                       #! category ve postu serializerslarda cagirdigimiz icin oradan tekrar cagirabiliriz.
    PostSerializer,
    )


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer