from django.db import models

# Create your models here.

class Flight(models.Model):
    flight_number=models.CharField(max_length=50)
    operation_airlines=models.CharField(max_length=50)
    departure_city=models.CharField(max_length=50)
    arrival_city=models.CharField(max_length=50)
    date_departure=models.DateTimeField()               #! auto_now_add=True bu option sadece created datelerde lazim. 
    estimated_time=models.TimeField()                   #! burada tarihler manuel olarak girilecegi icin auto_now_add yazmiyoruz.

    def __str__(self):
        return f"{self.flight_number} - {self.departure_city} - {self.arrival_city}"
    

class Passenger(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=models.IntegerField()
    create_date=models.DateTimeField(auto_now_add=True)                           

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    
from django.contrib.auth.models import User          #!
class Reservation(models.Model):
    #!bu reservasyonu hangi user gerceklestirdi diye sorarsak kendimize nasill basliyacagimizi buluruz.
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    #!bu rezervation hangi Flight icin yapildi
    flight=models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="reservation")
    #! bu reservation hangi yolcu icin yapildi
    passenger=models.ManyToManyField(Passenger, related_name="reservation")       #!manytomanyField extra tablo olusturur. db e bak


#todo admin panele ekle.