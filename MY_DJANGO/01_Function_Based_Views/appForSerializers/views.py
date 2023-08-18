from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Student2,Path

from .serializers import Student2Serializer, PathSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#! Http Response import et.
#! get_object_or_404 import et.
#! modelsleri import et.
#! serializerslari import et. 

# Create your views here.  #!step:3    serializers olusturduktan sonra buraya gel..

def home(request):
    return HttpResponse("<h1>API page</h1>")

@api_view(["GET", "POST"])   #!decarator
def student2_api(request):
    if request.method =="GET":
        students = Student2.objects.all()
        serializer = Student2Serializer(students, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = Student2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"
                }
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(["GET", "PUT", "DELETE", "PATCH"])
def student2_api_get_update_delete(request,pk):
    student = get_object_or_404(Student2, pk=pk)
    if request.method == 'GET':
        serializer = Student2Serializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = Student2Serializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = Student2Serializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)
    

@api_view(['GET', 'POST'])
def path_api(request):
    # from pprint import pprint
    # pprint(request)
    if request.method == 'GET':
        paths = Path.objects.all()
        serializer = PathSerializer(paths, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PathSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Path saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




