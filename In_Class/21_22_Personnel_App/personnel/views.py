from django.shortcuts import render

# Create your views here.
#!1808  10:47 

from .serializers import Department, DepartmentSerializer, Personnel, PersonnelSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.permissions import IsAdminUser ,IsAuthenticatedOrReadOnly                 #!1808 11:15  Pause...
from .permissons import IsStaffOrReadOnly                           #! 1808 11:58
from rest_framework.response import Response
from rest_framework import status



class DepartmentView(ListCreateAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    # permission_classes=[IsAdminUser]                                #!1808 11:49   dann create permissons.py 
    permission_classes=[IsStaffOrReadOnly]                          #! 1808 11:58   git ve kontrol et admin disindaki insanlarla post islemini görebiliyormuyum. 

class PersonnelView(ListCreateAPIView):
    queryset=Personnel.objects.all()
    serializer_class=PersonnelSerializer
    permission_classes=[IsAdminUser]
    # permission_classes=[IsStaffOrReadOnly]                           #! 1808 11:58


class Personnel_GPD_View(RetrieveUpdateDestroyAPIView):      #! 1808 12:10   go to urls.py dann go to postman
    queryset=Personnel.objects.all()
    serializer_class=PersonnelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#!1808 12:21 yeni seyler ekliyor hoca buraya.... ekledimmm  # Bu alana bi göz at. hocayi tekrar dinle.......
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.is_staff and (instance.create_user == self.request.user):
            return self.update(request, *args, **kwargs)
        else:
            data = {
                "message": "You are not authorized to perform this operation"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        else:
            data = {
                "message": "You are not authorized to perform this operation"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
#!1808 ----------------------------------------------------------------------------------------------

#!1808 12:28  son alan olabilir. hoca copy ile geldi.------------------------------------------------ 
class DepartmentPersonnelView(ListAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    
    def get_queryset(self):
        name = self.kwargs["department"]
        return Department.objects.filter(name__iexact=name)

#!1808 12:30 go to urls
#!1808 12:30 go to serializers 13.line
#!---------------------------------------------------------------------------------------------------

#!1808  10:55 go to main/urls.py 

