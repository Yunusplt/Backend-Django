from django.urls import path
from .views import dswelcome


urlpatterns = [
    path('', dswelcome), 
]