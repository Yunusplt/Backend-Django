from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to DTL (Django Template Language)</h1>")


def body(request):
    context = {
        "title":"clarusway",
        "path":"FS",
        "list": ["yunus","ozlem","fatih","esra","huseyin","nihal","emirhan","halit","irfan"],
        "dict": {
            "k1" : "value1",
            "k2" : "value2"
            },
        "number" : 0,
        "desc":"this template from APP."
        }
    return render(request,"templateApp/index.html", context)
    # return render({"name":"yunus"} , request="index.html")