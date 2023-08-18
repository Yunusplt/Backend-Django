from django.db import models

#todo bu app sadece model icin olusturuldu. view ve urls yok. Admin file ina bak...

# Create your models here.

class Student(models.Model):
    COHORTS=(
        ("FS","FullStack"),
        ("DS","DataScience"),
        ("AWS","AWS DevOps")
    )

    first_name=models.CharField(max_length=30)             #!CharField'da max_length zorunlu
    last_name=models.CharField(max_length=30)
    number=models.IntegerField()
    cohort=models.CharField(max_length=3, choices=COHORTS, default="FS")   #! buradaki max_length keylerdeki en uzun key e esit.
    email=models.EmailField(null=True)
    register_date=models.DateTimeField(auto_now_add=True, null=True)        #! tarih ilkkez ekleniyorsa auto_now_add        
    update_date=models.DateTimeField(auto_now=True, null=True)              #! güncelleme yapiliyorsa auto_now 
    is_active=models.BooleanField(default=True)
    comment=models.TextField(null=True)

    def __str__(self):                            #! admin panelde student_object(1) yerine name and lastname yazmasini sagliyoruz.
        return f"{self.first_name} - {self.last_name}" 
    
    class Meta:                                
        ordering=["first_name"]                #!siralamayi degistirmek icin bu kullanilir. yani basina - koydugum zaman first-name leri z-a ya göre siralar. yunus 1. sirada Nihal 2.sirada olur.
        verbose_name_plural="Student List"     #! admin panelde tablo ismi degistirir.


#! Model olusturduktan sonraki adimlar:
#? python manage.py makemigrations
#? python manage.py migrate
#? veri tabanini silmek zorunda kalirsam tekrar migrate yapmaliyim
#? veri tabaninda bir degisiklikten sonra sikinti cikmamsi icin veri tabanini sil. migrations dosyasi icinden 0001_initiali da sil
#? daha sonra yukaridaki komutlari yeniden gir.
#? model dosyasi bittikten sonra admin.py dosyasina git.