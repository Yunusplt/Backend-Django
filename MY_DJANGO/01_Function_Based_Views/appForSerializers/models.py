from django.db import models

# Create your models here. #! step:1

class Path(models.Model):
    path_name=models.CharField(max_length=50)
    #! student                                    # 11. satirdaki kod ile burada student varmis gibi davraniyor
    def __str__(self):
        return self.path_name

class Student2(models.Model):
    path=models.ForeignKey(Path, related_name="students", on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)              #! fieldname = fieldtype(fieldoptions)
    last_name=models.CharField(max_length=50)               
    number=models.IntegerField(blank=True, null=True)       #! blank true yazdigi zaman bu field frontend den bos olarak gönderilebilir. null=True yazdgi icin de default olarak null atanir. 
    age=models.IntegerField()

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    

#todo fieldTypes https://docs.djangoproject.com/en/4.2/topics/db/models/
#todo fieldTypes on_delete=CASCADE oldugu zaman. pathdeki AWSDevOps u sildigim zaman. student modeldeki AWSDevOps pathine sahip ögrenciler de siliniyor.
 

#! modeli olusturdum ilk adim 
#! setting.py da app i tanimla
#! admin.py da modelleri tanimla
#! makemigrations
#! migrate



