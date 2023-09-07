from django.db import models
from django.contrib.auth.models import User
#!for validation
from django.core.validators import MinValueValidator
# Create your models here.
#! FixField farkliiii hepsinde olan ortak fieldler buraya yaziliyor...
class FixField(models.Model):
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    #!eger abstract esittir true demezseniz yeni model olusturur. 
    class Meta:
        abstract=True




class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name=models.CharField(max_length=30)
    image=models.TextField()

    def __str__(self):
        return self.name
    

class Product(FixField):
    name=models.CharField(max_length=30)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='c_products')
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='b_products')
    stock=models.SmallIntegerField(blank=True, null=True, default=0)
    # created=models.DateField(auto_now_add=True)
    # updated=models.DateField(auto_now=True)
    #! artik created ve updated kommt aus FixField

    def __str__(self):
        return self.name
    

class Firm(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    image=models.TextField()

    def __str__(self):
        return self.name
    

class Purchases(FixField):
    #! normalde on_delete nulls daha mantikli. 
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    firm=models.ForeignKey(User, on_delete=models.CASCADE, related_name='f_purchases')
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='b_purchases')
    product=models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='p_purchases')
    quantity=models.SmallIntegerField()
    price=models.DecimalField(max_digits=8, validators=[MinValueValidator(0)], decimal_places=2)
    price_total=models.DecimalField(max_digits=8, validators=[MinValueValidator(0)], decimal_places=2)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity}"


class Sales(FixField):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='b_sales')
    product=models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='p_sales')
    quantity=models.SmallIntegerField()
    price=models.DecimalField(max_digits=8, validators=[MinValueValidator(0)], decimal_places=2)
    price_total=models.DecimalField(max_digits=8, validators=[MinValueValidator(0)], decimal_places=2)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity}"
