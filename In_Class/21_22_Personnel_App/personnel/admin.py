from django.contrib import admin

# Register your models here.
#!18.08   10:35

from .models import Department, Personnel

admin.site.register(Department)
admin.site.register(Personnel)

#!18.08   10:36     makemigrations migrate (suan database de gözlemlenebilir...)
#!18.08   10:37     go to admin panel and add a pair personnel... then go to serializers