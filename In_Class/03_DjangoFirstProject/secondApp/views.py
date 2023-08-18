from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome2(request):
    return HttpResponse("ikinci app e hosgeldiniz")