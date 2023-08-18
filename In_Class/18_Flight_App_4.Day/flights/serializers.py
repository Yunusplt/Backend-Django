from rest_framework import serializers
from .models import *


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        exclude =[]

class ReservationSerializer(serializers.ModelSerializer):
    #! views daki hatadan sonra hoca buraya ekleme yapiyor. 
    #! hocanin burada yaptigi degisiklik bir kac önceki derslerden id ve isim tanimlama ile ayni olabilir. dön bak..frontent isim backedn is ihtiyaci duyar konusu
    class Meta:
        model = Reservation
        exclude =[]

class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        exclude =[]
    





#todo views a git.