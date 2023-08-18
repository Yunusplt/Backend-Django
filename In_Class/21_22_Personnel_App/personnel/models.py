from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#!1808 09:50 -------------------------------------------------------
class Department(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

#!1808 10:00 Pause ------------------------------------------------- 
#!1808 10:20 -------------------------------------------------------
class Personnel(models.Model):
    GENDERS=(
        ("M","Male"),
        ("F","Female"),
        ("O","Other"),
        ("X","Prefer not to say"),
    )

    TITLES=(
        (1,"Menager"),
        (2,"Team Lead"),
        (3,"Developer"),
        (4,"Junior"),
    )
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="personnels")  #! bir departmentda bir cok kisi calisabilir. ForeignKey. Department silindigi zaman personelin Department field i 0 olsun sete_null ile
    #!1808 11:09 parentden buraya ulasmak istedigim icin related_name veriyoruzr.
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=1, choices=GENDERS)
    title=models.IntegerField(choices=TITLES)
    salary=models.IntegerField(default=1000)
    start_date=models.DateTimeField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.first_name}"
    
#! go to admin.py