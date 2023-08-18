from django.db import models

class Path(models.Model):                                  #todo 2. model olusturduk studentten sonra 
    path_name = models.CharField(max_length=50)
    #!student   burada student varmis gibi algiliyor. asagida yapilan islemle.
    def __str__(self):
        return f"{self.path_name}"


class Student(models.Model):  
    path = models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE)                               
    first_name = models.CharField(max_length=30)            #! fieldname = fieldType(fieldOptions)
    last_name = models.CharField(max_length=30)             #! blank yazmazsa frontentten post ederken o fieldler dolu olmak zorunda.
    number = models.IntegerField(blank=True, null=True)     #! blank true yazdigi zaman o field eksik sekilde frontend den post edilebilir ve null=True oldugu icin de karsisina deger olarak null atanir.
    age = models.IntegerField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
