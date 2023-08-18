from django.db import models

# Create your models here.
#!models class ile olusturulur.

class Path(models.Model):
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return self.path_name
    
class Student(models.Model):
    path = models.ForeignKey(Path, related_name="students", on_delete=models.CASCADE)   #!buradaki students serializers 23. satirdaki ile ayni olmak zorunda
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField(blank=True, null=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    

#todo- todo models örnegi (09_Task_Tracker) bakilabilir. farkli bir örnek icin 
#