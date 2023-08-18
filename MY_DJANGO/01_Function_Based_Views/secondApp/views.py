from django.shortcuts import render
from django.http import HttpResponse         #todo secondApp i include ile sergilemek icin ilk adim. daha sonra secondApp in kendisi icin URl dosyasi olusturuyoruz. 

# Create your views here.

def contact(request):
    return HttpResponse("<h1>This is secondApp. it was created with include url.</h1>")