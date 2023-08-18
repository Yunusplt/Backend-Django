#26.07.2023 09:43
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.


def home(request):
    return HttpResponse('<h1>API Page</h1>')
##############################################################################################################

#!http methods
# GET
# POST
# DELETE
# PUT
# PATCH
# tüm fullstack django ile olusturulacaksa get ve post yeterli.

@api_view(["GET"])
def student_api(request):
    students=Student.objects.all()                               #veri type queryset
    serializer=StudentSerializer(students, many=True)            #serialzers
    return Response(serializer.data)                             # neyi döndürcek. serializersin islem yaptigi datayi #query seti alip sjson formatinda döndürüyor.

@api_view(["GET"])
def student_detail(request,pk):
    student = get_object_or_404(Student, pk=pk)       #todo try catch gibi calisir. 
    serializer = StudentSerializer(student)            #todo####################### serializer sartttt
    message = {"Successfull"}
    data = {}
    data["message"] = message
    data["data"]=serializer.data
    return Response(data)

@api_view(["POST"])
def student_create(request):
    # print(request.data)
    # return Response("deneme")
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():        # gelen veriyi kontrolden geciriyorum dogru mu degil mi/ modelsteki kendi olusturdugumuz yapiya uyuyor mu gönderdigimiz veri omnu kontrool ediyor. 11line in models.py
        serializer.save()
        message={"message":"Successfully Created"}
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def student_delete(request,pk):         
    # student=Student.objects.get(id=pk)
    student = get_object_or_404(Student, pk=pk)
    student.delete() 
    message={"message":"Successfully Deleted"}     
    return Response(message) 

# @api_view(["PUT"])
@api_view(["PATCH"])
def student_update(request, pk):
    student=get_object_or_404(Student, pk=pk)
    # PUT
    # serializer = StudentSerializer(instance=student, data=request.data)
    serializer = StudentSerializer(instance=student, data=request.data , partial=True)
    if serializer.is_valid():
        serializer.save()
        message={"message":"Successfully Updated"}
        return Response(message)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

##############################################################################################################

#! Class Based Views  #####################################################################

#!API View Class

class StudentListCreate(APIView):                                    #todo önce APIView import ettik. 
       
    def get(self,request):                                           #todo mehodlarimiz get ve post..
        students=Student.objects.all()                               #todo yukardan koyaladik. 
        serializer=StudentSerializer(students, many=True)            
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)              #todo yukaridan kopyaladim.
        if serializer.is_valid():        
            serializer.save()
            message={"message":"Successfully Created"}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    
    def get_obj(self, pk):
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(data=request.data, instance=student)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(data=request.data, instance=student, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        student = self.get_obj(pk)
        student.delete()
        data = {
            'message': 'Student succesfully deleted.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
#todo bunuda inherit ederek olusturabilirdim. GenericAPIView in yaptiginin aynisini burada da yapabilriim aslinda.
class newStudentListCreate(StudentListCreate):
    pass
    
##############################################################################################################

#! Generic APIView and Mixins ################################################################################


#GenericAPIView
""" One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior. 
REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

GenericAPIView class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views. 
Some Basic Attributes and Methods. """


#mixins
""" The mixin classes provide the actions that are used to provide the basic view behavior. 
Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post(), directly. 
This allows for more flexible composition of behavior. Tek başlarina bir işlem yapamazlar. GenericAPIView ile anlamli oluyor """


class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin,GenericAPIView):  #todo mixinsler tek basina kullanilamaz genericAPIView s e ihtiyaci var.
    queryset = Student.objects.all()
    serializer_class = StudentSerializer                                    #todo queryset ve serializer class override ettik.. özellestirmek icin


    def get(self,request,*args, **kwargs):                                  #todo burasi mesela calisacak. ben 164ve165 te override etmeseydim. inheritance edilen yerdeki calisacakti ama suan kendi classi icine bakyior ve burada oldugu icin burasi calisiyor. 
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    

class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,GenericAPIView):  
    queryset = Student.objects.all()
    serializer_class = StudentSerializer                              


    def get(self,request,*args, **kwargs):                                 
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    
    def delete(self,request,*args, **kwargs):
        return self.delete(request,*args, **kwargs)
    
#!yine bir miras örnegi  #####################################################

class myStudentClass(StudentGAV):  #todo kendi yazdigim classi burada inherit ettim ve tüm özelliklerini burada kullanabilirim. 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer             #todo burada da overriding ediyorum.
#! ##########################################################################################################

#! Concrete View Classes

class StudentCV(ListCreateAPIView):        #todo tüm get ve post burada 3 satirda yapiliyor. OPP de ki abstraction mantigi budur. soyutladi bizi gereksiz kavramlardan.
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailCV(RetrieveUpdateDestroyAPIView):      
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#! ViewSets

'''aciklama var burada'''

class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #!method yaziyoruz
    @action(detail=False, methods=["GET"])
    def student_count(self,request):
        count={
            "student-count" : self.queryset.count(),
        }
        return Response(count)
    
class PathMVS(ModelViewSet):
    
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    @action(detail=True)
    def student_names(self, request, pk=None):
        path = self.get_object()
        students = path.students.all()
        return Response([i.first_name for i in students])
