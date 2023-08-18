
#todo bu klasör manuel olusturdum.  #################     3
from django.urls import path
from .views import home,student_api,student_api_get_update_delete,path_api        #todo  ########### home-- viewden dön home import et         8

urlpatterns = [
    #path('admin/', #views),     #todo #########################################   4
    path("", home),         #todo  ##############################            9  artik browserda endpoint  /api/home oldu....
    path("student/", student_api),                                           #todo serializers 
    path("student/<int:pk>", student_api_get_update_delete, name="detail"),
    path("path/",path_api),
]

#todo