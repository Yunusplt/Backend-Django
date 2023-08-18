from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Personel(models.Model):
    GENDERS=(
        ("1","Male"),
        ("2","Female"),
        ("3","Other"),
        ("4","Prefer not to say"),
    )

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=1, choices=GENDERS, default="4")
    title=models.CharField(max_length=50)
    salary=models.IntegerField(blank=True, null=True)
    started=models.DateTimeField()
    department=models.ForeignKey(Department, on_delete=models.CASCADE, related_name="x")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    
