
from django.urls import path,include
from .views import blog, CategoryMVS, PostMVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register("category", CategoryMVS)
router.register("post", PostMVS)



urlpatterns = [
    path('', blog ),
    path("", include(router.urls))
]