from django.urls import path
from .views import contact                  #! step:2   secondApp'in views ini buraya cekiyoruz.

urlpatterns = [
    path('', contact),                      #! step:3 burada tanimliyoruz. ve main klosöründeki urls dosyasina gidiyoruz. 
]