from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.status import *

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Todo APP</h1></center>'
    )

#! FBV #########################################################################################

@api_view(["GET","POST"])
def todo_list_create(request):
    if request.method=="GET":
        todos=Todo.objects.all()                       #todo todo modelimin hepsi gelsin. 
        serializer=TodoSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message={"message":"Successfully Created"}
            return Response(message, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","DELETE"])
def todo_get_delete_update(request,pk):
    if request.method=="GET":
        todo=get_object_or_404(Todo, pk=pk)                       #todo todo modelimin hepsi gelsin. 
        serializer=TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer=TodoSerializer(data=request.data, instance=todo)
        if serializer.is_valid():
            serializer.save()
            message={"message" :"successfuly"}
            return Response(message, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        todo=get_object_or_404(Todo, pk=pk)
        todo.delete()
        message={"message":"Successfully Deleted"}     
        return Response(message, status=HTTP_202_ACCEPTED)
    
#!#########################################################################################
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
#! CBV

class Todos(ListCreateAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

class TodosRUD(RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    # lookup_field=id

#! MVS
from rest_framework.viewsets import ModelViewSet
class TodosMVS(ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
