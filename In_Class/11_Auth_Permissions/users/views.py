from django.shortcuts import render                           #!0108
from rest_framework.generics import (CreateAPIView)          
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view



# Create your views here.

class RegisterView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer


    def perform_create(self, serializer):
        user = serializer.save()
        return user

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        token = Token.objects.create(user_id=user.id)
        data=serializer.data
        data["token"]=token.key
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "created successfully", "details": data}, status=status.HTTP_201_CREATED, headers=headers)
    



@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            # Oturum açmış kullanıcının auth_token'ını silin
            request.user.auth_token.delete()
            data = {
                'message': 'logout succeeded'
            }
            return Response(data)
        else:
            # Eğer kullanıcı oturum açmamışsa işlem yapmaya gerek yok
            return Response({'message': 'User is not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
