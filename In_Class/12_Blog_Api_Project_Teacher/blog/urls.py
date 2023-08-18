from rest_framework.routers import DefaultRouter
from .views import CategoryView, PostView

#!Router
router = DefaultRouter()
router.register("category", CategoryView)
router.register("post", PostView)

# urlpatterns = [
#     path('', include('router.urls'))
# ]

urlpatterns = router.urls      #! urlpatternin ici dolu olsaydo + - ile ekliyecektik. 
