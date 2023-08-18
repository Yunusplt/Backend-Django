#26.07.2023 09:43
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def home(request):
    return HttpResponse('<h1>API Page</h1>')

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
    student = get_object_or_404(Student, pk=pk)
    message = {"message":"Successfull"}
    return Response(message)

@api_view(["POST"])
def student_create(request):
    # print(request.data)
    # return Response("deneme")
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():        # gelen veriyi kontrolden geciriyorum dogru mu degil mi
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