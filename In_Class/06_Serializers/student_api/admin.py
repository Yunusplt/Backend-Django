from django.contrib import admin
from .models import Student,Path          #todo studenti adminde görmek icin 1. adim 
# Register your models here.

admin.site.register(Student)        #todo 2. adim ###########
admin.site.register(Path)