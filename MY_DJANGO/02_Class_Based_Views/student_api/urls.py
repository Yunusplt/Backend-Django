
from django.urls import path
from .views import (
    home,

    #!APIView
    StudentListCreate,
    StudentDetail,

    #!GenericAPIView
    StudentGAV,
    StudentDetailGAV,

    #!Concrete View Classes
    StudentCV,
    StudentDetailCV,

    #!ModelViewSets
    StudentMVS,
    PathMVS,
    
    )


urlpatterns = [
   path('', home),
   # path('list', StudentListCreate.as_view()),              #!APIView         #Class based view ise .as_view() sart
   # path('detail/<int:pk>', StudentDetail.as_view()),       #!APIView
   # path('list', StudentGAV.as_view()),                     #!GenericAPIView
   # path('detail/<int:pk>', StudentDetailGAV.as_view()),    #!GenericAPIView
   # path('list', StudentCV.as_view()),                      #!Concrete View Classes
   # path('detail/<int:pk>', StudentDetailCV.as_view()),     #!Concrete View Classes
   # path('list', StudentMVS.as_view()),                     #!ModelViewSets  #as_view bunlarda calismadi 38-48 arasi
   # path('path', PathMVS.as_view()),                        #!ModelViewSets  #as_view bunlarda calismadi 38-48 arasi
   
]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("student", StudentMVS)
router.register("path", PathMVS)                #!http://127.0.0.1:8000/api/path/2/student_names/   students_names method name

urlpatterns += router.urls