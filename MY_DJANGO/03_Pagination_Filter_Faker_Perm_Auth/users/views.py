from django.shortcuts import render                           #!0108
from rest_framework.generics import (CreateAPIView)          
from django.contrib.auth.models import User
from .serializers import UserSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token            #!self.perform_create(serializer)  bunu user a atadiktan sonra Token import et 
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet



#!KADIR HOCA #######################################################################################################
from rest_framework.permissions import IsAdminUser

class UserMVS(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = IsAdminUser                  #! Globalde login olan herkes görsün dedik. ama userlari sadece adminler görsün diye burada local olarak ayarladik.

#!buraya kadarki alanda register yapiyor. ama token olusturmuyor. 
#!Override yapicaz


#!SINANHOCA##########################################################################################################

# class RegisterView(CreateAPIView):
#     queryset=User.objects.all()
#     serializer_class=RegisterSerializer
# #! buraya kadarki alanda register yapiyor. ben register yaparken loginde yapsin istiyorum ve token olustursun istiyorum. 

#     def perform_create(self, serializer):
#         user = serializer.save()
#         return user
# #todo asagidaki create blogu nereden geldi? CreateApiView tikla sonra Mixin e tikla orada var. aldik ve custom ettttik . 
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         #self.perform_create(serializer)                    #! burada create islemi gerceklesiyor. token olusturmak icin bunu bir degiskene atmaliyim .
#         user = self.perform_create(serializer)              #! bundan sonra token import et      
#         token = Token.objects.create(user_id=user.id)       #! token tanimla (user_id -> tokenin user id si) az önce olusturdugumuz userin id sini alsin (user.id)
#         data=serializer.data                                #!
#         data["token"]=token.key                             #!
#         headers = self.get_success_headers(serializer.data)
#         return Response({"message": "created successfully", "details": data}, status=status.HTTP_201_CREATED, headers=headers)
    



# @api_view(['POST'])
# def logout_view(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             # Oturum açmış kullanıcının auth_token'ını silin
#             request.user.auth_token.delete()
#             data = {
#                 'message': 'logout succeeded'
#             }
#             return Response(data)
#         else:
#             # Eğer kullanıcı oturum açmamışsa işlem yapmaya gerek yok
#             return Response({'message': 'User is not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
