from django.urls import path,include
from .views import TutorialMVS
from rest_framework.routers import DefaultRouter
 
router = DefaultRouter()
router.register("tutorials",TutorialMVS)

urlpatterns = [
    
]

urlpatterns += router.urls