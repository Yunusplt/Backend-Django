from django.shortcuts import render
from django.http import HttpResponse   #http yi return a yazmak icin import ediyoruz.
# Create your views here.
def welcome(request):
    return HttpResponse("<h1>Herzlich Willkommen</h1>")