from django.contrib import admin
from .models import Account,Adress,Product,Profile
# Register your models here.
admin.site.register(Account)
admin.site.register(Adress)
admin.site.register(Product)
admin.site.register(Profile)