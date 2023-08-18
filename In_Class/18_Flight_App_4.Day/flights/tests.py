from django.test import TestCase

# Create your tests here.
#! Api tests case kullancaz.
#! Class isminin sonu TestCase olmak zorunda.
#! functionslar da test ile baslamak zorunda.


from rest_framework.test import APITestCase,APIRequestFactory,force_authenticate
from .views import FlightMVS
from django.contrib.auth.models import AnonymousUser,User
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Flight


class FlightTestCase(APITestCase):
    def setUp(self):
        self.factory=APIRequestFactory()
        self.user=User.objects.create_user(
            username='yunus',
            email='yunus@gmail.com',
            password='321'
        )
        self.token=Token.objects.get(user=self.user)

        self.flight=Flight.objects.create( 
            id=1, 
            flight_number="AA100", 
            operation_airlines="AHY", 
            departure_city="Antalya", 
            arrival_city="Amsterdam", 
            date_departure="2022-12-01", 
            estimated_time="15:00:00"
            )
  
    def test_flight_list_as_guest(self):
        request=self.factory.get('flights')
        response=FlightMVS.as_view({"get":"list"})(request)
        request.user=AnonymousUser
        self.assertEqual(response.status_code, status.HTTP_200_OK)      #! 200 gelmesini basarili olmasini bekliyorum. o yuzden 200yazdik. gelen 200 e esitse dogru.


    def test_flight_create_as_guest(self):
        request=self.factory.post('flights')
        response=FlightMVS.as_view({"post":"create"})(request)
        request.user=AnonymousUser
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_flight_create_as_login(self):
        request = self.factory.put('/flights', HTTP_AUTHORIZATION='Token ' + self.token.key)
        response=FlightMVS.as_view({'post': 'create'})(request)
        # request.user=AnonymousUser
        self.assertEqual(response.status_code,403)

    def test_flight_create_as_admin(self):
        data = {
             "flight_number": "TK100",
             "operation_airlines": "THY",
             "departure_city": "Antalya",
             "arrival_city": "Amsterdam",
             "date_departure": "2022-12-03",
             "estimated_time": "15:27:22"
        }
    
        request = self.factory.post('/flights/', data, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.user.is_staff=True
        self.user.save()
        force_authenticate(request, user=self.user)
        response=FlightMVS.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code,201)


    def test_flight_update_as_admin(self):
        data = {
             "flight_number": "TK100",
             "operation_airlines": "Luft",
             "departure_city": "Berlin",
             "arrival_city": "Amsterdam",
             "date_departure": "2022-12-03",
             "estimated_time": "15:27:22"
        }
    
        request = self.factory.put('/flights/1', data, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.user.is_staff=True
        self.user.save()
        force_authenticate(request, user=self.user)
        response=FlightMVS.as_view({'put': 'update'})(request,pk="1")
        self.assertEqual(response.status_code,200)

    def test_flight_str_all(self):
        self.assertEqual(str(self.flight),f"{self.flight.flight_number} - {self.flight.departure_city} - {self.flight.arrival_city}")

