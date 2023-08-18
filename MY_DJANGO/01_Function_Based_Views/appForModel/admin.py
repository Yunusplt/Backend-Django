from django.contrib import admin
from .models import Student              #! step:2 model olusturulduktan sonra. model ismi burada import edilir.. admin panelde gözükmesi icin.


# Register your models here.
admin.site.register(Student)             #! step:3 Student modeli admine tanimlandi.