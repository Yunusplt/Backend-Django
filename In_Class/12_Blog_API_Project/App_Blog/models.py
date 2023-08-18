from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Blog Kategori'
        verbose_name_plural = 'Blog Kategoriler'

    def __str__(self):
        return self.name

class Post(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog Yazisi'
        verbose_name_plural = 'Blog Yazilari'
        ordering=["title"]


