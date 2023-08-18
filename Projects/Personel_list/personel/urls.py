
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DepartureMVS,PersonelMVS

router = DefaultRouter()
router.register("personel", PersonelMVS )
router.register("departure", DepartureMVS )



urlpatterns = [
    path("", include(router.urls)),
]