from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1> Welcome to student_api Page </h1>")


#!########################### CLASS BASED VIEWS #############################################

#!--------------APIViews Class--------------------
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student,Path
from .serializers import StudentSerializer, PathSerializer
from django.shortcuts import get_object_or_404

class StudentListCreate(APIView):

    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message={"message":"Successfully Created"}
            return Response(message,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):

    def get(self,request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def patch(self,request,pk):
        student = get_object_or_404(Student,pk=pk)
        serializer = StudentSerializer(data=request.data, instance=student , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        data = {
            'message': 'Student succesfully deleted.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
#!##################################################################################################

#! ------------------Generic APIView and Mixins-------------------------
""" One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior. REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

GenericAPIView class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views. Some Basic Attributes and Methods. """


#mixins
""" The mixin classes provide the actions that are used to provide the basic view behavior. Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post(), directly. This allows for more flexible composition of behavior. Tek başlarina bir işlem yapamazlar. GenericAPIView ile anlamli oluyor """

from rest_framework.generics import GenericAPIView, mixins

class StudentGAV( mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):  #!GAV GenericApiView
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

#!##########################################################################################

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

#! Concrete View Classes

class StudentCV(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#!##########################################################################################


from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

#! ModelViewSets 

""" - Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet. 

- Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a router class, that automatically determines the urlconf for you.

There are two main advantages of using a ViewSet class over using a View class.

 - Repeated logic can be combined into a single class. In the above example, we only need to specify the queryset once, and it'll be used across multiple views.
 - By using routers, we no longer need to deal with wiring up the URL conf ourselves.

Both of these come with a trade-off. Using regular views and URL confs is more explicit and gives you more control. ViewSets are helpful if you want to get up and running quickly, or when you have a large API and you want to enforce a consistent URL configuration throughout. """

class StudentMVS(ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
    @action(detail=False, methods=["GET"])
    def student_count(self, request):                      #! ögrenci sayisini döndürecek bir method yaziyoruz. method ismi = url_path in defaultRouter
        # print(dir(self.queryset))
        # print("hello")
        count  = {
            "student-count" : self.queryset.count(),
        }
        return Response(count)
    
    
class PathMVS(ModelViewSet):
    
    queryset = Path.objects.all()
    serializer_class = PathSerializer
    
    #!action ModelViewSet lere has bir özelliktir.
    @action(detail=True)                                    #!belli bir path i sececegim icin detail=True diyorum. defualt method get onu da belirtmiyorum parantez icinde.
    def student_names(self, request, pk=None):
        path = self.get_object()                            #!get_object()
        students = path.students.all()                      #! parentten childa related_name ile ulasilir. 
        return Response([i.first_name for i in students])
    
    #!http://127.0.0.1:8000/api/path/2/student_names/
    

#!##################################################################################

