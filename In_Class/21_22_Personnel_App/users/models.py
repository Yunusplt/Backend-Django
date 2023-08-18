from django.db import models

# Create your models here.
#! 1708 Eger Djangonun kendi user modelini kullanmayacaksaniz asagidaki gibi abstractUser inherit edip kendi modelinizi olusturabilir. ardindan bunu settings.py or in base.py da en altta tanimlamalisinniz.  AUTH_USER_MODEL = "users.MyUser"
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from datetime import date
# class MyUser(AbstractUser):
#     username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#     email = models.EmailField(('email address'), unique = True)
#     native_name = models.CharField(max_length = 5)
#     phone_no = models.CharField(max_length = 10)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#     def __str__(self):
#       return "{}".format(self.email)

from django.contrib.auth.models import User

class Profile(models.Model):
    #! user silinince Profile da siliniyor. 
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="pictures/", default="/pictures/avatar.png")
    about=models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"
#! install Pillow because we use imagefield
#! and go to base.py (setting.py)
#! and go to main urls.py 
