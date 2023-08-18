from django.db import models

#todo bu sefer birden fazla models olusturacaz.
# Create your models here.

class Account(models.Model):
    username=models.CharField(max_length=50)         #! username > fieldname 
    email=models.EmailField(null=True)               #! CharField > fieldtype
    password=models.CharField(max_length=50)         #! (parantez ici) > fieldoptions 

    def __str__(self):
        return self.username 
    
class Profile(models.Model):
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    about=models.TextField(null=True)
    phone=models.BigIntegerField(null=True)
    avatar=models.ImageField('userpicture', blank=True, null=True, upload_to=("media/"))
    account=models.OneToOneField(Account, on_delete=models.DO_NOTHING)    #? account ile birlestirme like foreignkey  
    #CASCADE        ile primarykey silidigi zaman foreign de siliniyor. 
    #set_NULL       null olarak günceller. (account id (foreign key)yi sifirlar)
    #Do_Nothing     field oldugu gibi kalir

    #?resimle ilgili atilmasi gereken adimlar.
    # pillow paketini kur
    #   python -m pip install Pillow
    # settings.py a ekle STATIC_URL altina
    #   MEDIA_URL = 'media/
    # urls.py a ekle
    #   from django.conf import settings
    #   from django.conf.urls.static import static
    #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #yeni paket kurdugum icin en son 
    #pip freeze > requirements.txt

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="profile about user"
        verbose_name_plural="Users Profile"


class Adress(models.Model):
    name=models.CharField(max_length=20)
    adress=models.TextField(null=True)
    account=models.ForeignKey(Account, on_delete=models.CASCADE)
    #? yukardakinden farki ne? bir kullanicinin birden fazla adresi olabilir o yuzden foreignkey.  

    def __str__(self):
        return self.name
    

class Product(models.Model):
    productname=models.CharField(max_length=20)
    account=models.ManyToManyField(Account)
    def __str__(self):
        return self.productname

#todo herseyi tamamladiktan sonra appi setting.py eklemeyi unutma