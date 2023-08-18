#!djrestauth kullanacaz ilerde....

#!KADIR HOCA ############################################################################
from django.urls import path  
from rest_framework.routers import DefaultRouter
from .views import UserMVS

#------------------------------------------------------------------------
#login
from rest_framework.authtoken.views import obtain_auth_token

#------------------------------------------------------------------------
#logout
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def logout(request):
    #! print(dir(request))                 !!!!!!!!!!! ÖNEMLI
    request.user.auth_token.delete()    #! Token Silmek demek logout demek 
    return Response({"message": 'User Logout: Token Deleted'})


urlpatterns =[
    path('login/', obtain_auth_token),
    path('logout/', logout),
]


router = DefaultRouter()
router.register("", UserMVS)

urlpatterns += router.urls



#!SINAN HOCA#############################################################################

# from django.urls import path, include    #!0108
# from .views import RegisterView,logout_view
# from rest_framework.authtoken.views import obtain_auth_token

# urlpatterns = [
#     path("register", RegisterView.as_view()),           #!0108   class based viewlerde as_view sart
#     path("login", obtain_auth_token),          
#     path("logout", logout_view),          
# ]

#!#######################################################################################