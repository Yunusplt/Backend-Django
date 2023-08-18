"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include             #! secondApp step:4 include ihtiyacimiz var.
from .views import home                          #! homepage step:2
from firstApp.views import about                 #! firstApp step:2

urlpatterns = [
    path('admin/', admin.site.urls),             #default 
    path('', home),                              #! homepage step:3     //main.views.py
    path('about', about),                        #! firstApp step:3     //firstApp.views.py
    path('contact', include("secondApp.urls")),  #! secondApp step:5 include ile secondApp'e ait urls i tanimliyoruz.
    path("api/", include("appForSerializers.urls")),
    path("api2/", include("appForFBV.urls")),
]


#todo bu 3 satir. mediayi modele eklemek icin pillow install ettikten sonra. MEDIA_URL setting.py de tanimladiktan sonra burada yazildi
from django.conf import settings    
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#todo BURASI ANA SANTRALLLLL buradan applerime yönlendirme yapiyorum.
