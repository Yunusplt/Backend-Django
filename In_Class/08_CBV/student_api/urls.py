#26.07.2023 09:44
from django.urls import path,include
from rest_framework import routers    #! for view sets
from .views import (
    home,
    student_api,
    student_create,
    student_detail,
    student_delete,
    student_update,
    #!Class views
    StudentListCreate,
    StudentDetail,

    StudentGAV,
    StudentDetailGAV,

    StudentCV,
    StudentDetailCV,
    
    StudentMVS,
    PathMVS
    )

router = routers.DefaultRouter()         #todo defaultrouter bir classtir. (simplerouteri) inheritance yaparak olusmustur
router.register("student", StudentMVS)   #todo bir prefix tanimliyoruz "student"
router.register("path",PathMVS)

urlpatterns = [
    #! Function views endpoints
    # path("", home ),
    # path("student-list", student_api, name="liste" ),
    # path("student-create", student_create, name="create" ),
    # path("student-detail/<int:pk>",student_detail,name="detail"),      
    # path("student-delete/<int:pk>",student_delete,name="delete"),
    # path("student-update/<int:pk>",student_update,name="update")

    #!Class views endpoints
    # path("student/", StudentListCreate.as_view()),                 #todo class oldugu icin as_view ekliyoruz. 
    # path("student-detail/<int:pk>", StudentDetail.as_view())

    # path("student/", StudentGAV.as_view()),               
    # path("student-detail/<int:pk>", StudentDetailGAV.as_view())

    # path("student/", StudentCV.as_view()),                
    # path("student-detail/<int:pk>", StudentDetailCV.as_view()),
    # path("",include(router.urls))                                  #todo bu sekilde de routers yapisi kullanilabilir. 

] 

urlpatterns += router.urls 