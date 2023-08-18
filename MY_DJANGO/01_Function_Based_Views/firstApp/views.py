from django.shortcuts import render
from django.http import HttpResponse     #todo firstApp i ekrana yazdirmak icin ilk adim.

# Create your views here.

def about(request):
    return HttpResponse("<h1>This is firstApp. There is no include in Main.urls for this.</h1>")