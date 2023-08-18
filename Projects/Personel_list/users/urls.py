from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProfileMVS, UserMVS

router = DefaultRouter()
router.register("profile", ProfileMVS)
router.register("user", UserMVS)

urlpatterns = [
    path("", include(router.urls))
    
]