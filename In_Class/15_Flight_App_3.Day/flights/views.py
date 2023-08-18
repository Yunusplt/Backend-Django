from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.
#!ucuslara herkes tarafindan müdahale edilmesin 
# from rest_framework.permissions import Is bize uygun bulamadik .... #! admin olustursun digerleri okusun istiyoruz.
from .permissions import IsAdminOrReadOnly                            #! kendi olusturdugumuz permission i cagirdik.
from rest_framework.permissions import IsAuthenticated


class FlightMVS(ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    permission_classes=[IsAdminOrReadOnly]                            #! admin post yapsin digerleri okusun sadece


class ReservationMVS(ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    permission_classes=[IsAuthenticated]                            #? sorun var. postmanda calisiyor Browserda calismiyor.
    #!queryset i degistir. kullanici sadece kendi reservationlari görsün. suana kadar loginse herkesi görüyordu.
    #!asagidaki hatadan dolayi hoca serializersda ekleme yapiyor. 
    #! burada dersi biraktim 0808 12:00
    def get_queryset(self):  #!override
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)      


class PassengerMVS(ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer
    