from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):   #!model ile inherit ettikten sonra bu artik class degil model
    name=models.CharField(max_length=64)

    class Meta:
        verbose_name= 'Blog Kategori'
        verbose_name_plural = 'Blog Kategoriler'

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title=models.CharField(max_length=128)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'Blog Yazisi'
        verbose_name_plural = 'Blog Yazilari'

    def __str__(self):
        return f'{self.category} / {self.title}' 


