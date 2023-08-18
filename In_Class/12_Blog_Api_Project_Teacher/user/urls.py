from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserView

#!#########################################################
#!login
from rest_framework.authtoken.views import obtain_auth_token


#!#########################################################
#! Logout:
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['POST'])
def logout(request):
    #! print(dir(request))                 !!!!!!!!!!! ÖNEMLI
    request.user.auth_token.delete()    #! Token Sil.
    return Response({"message": 'User Logout: Token Deleted'})

#!###########################################################
#! url for Login/Logout
urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', logout),
]

#!Router
router = DefaultRouter()
router.register('', UserView)

urlpatterns += router.urls



# urlpatterns = router.urls      #! urlpatternin ici dolu olsaydo + - ile ekliyecektik. 31. line 
