from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register("fly",FlightMVS)
router.register("resv", ReservationMVS)


urlpatterns = [
    path('', include(router.urls)),
]


