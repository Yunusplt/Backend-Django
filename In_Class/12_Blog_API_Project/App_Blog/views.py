from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    return HttpResponse("<h1>Blog App</h1>")


from rest_framework.viewsets import ModelViewSet
from .models import Category, Post
from .serializers import CategorySerializer,PostSerializers


class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
class PostMVS(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

