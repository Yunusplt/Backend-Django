from django.urls import path
from .views import fswelcome


urlpatterns = [
    path('', fswelcome), 
]