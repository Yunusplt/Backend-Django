
#!step:4 main urlde include icinde tanimladiktan sonra buraya gel. 
from django.urls import path
from .views import home, student2_api, student2_api_get_update_delete, path_api

urlpatterns = [
    #path('admin/', #views),  
    path("", home),        
    path("student/", student2_api),                                         
    path("student/<int:pk>", student2_api_get_update_delete, name="detail"),
    path("path/",path_api),
]
