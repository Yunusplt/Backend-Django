
from django.urls import path, include    #!0108
from .views import RegisterView,logout_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register", RegisterView.as_view()),           #!0108   class based viewlerde as_view sart
    path("login", obtain_auth_token),          
    path("logout", logout_view),          
]