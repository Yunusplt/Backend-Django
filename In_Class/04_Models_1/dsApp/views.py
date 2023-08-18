from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dswelcome(request):
    return HttpResponse("Ds Sayfasina Hosgeldiniz")