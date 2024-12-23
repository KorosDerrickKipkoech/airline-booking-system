from rest_framework import viewsets, filters
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer
from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to the Airline Booking System!")
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['flight__flight_number']  # Filter passengers by flight number
