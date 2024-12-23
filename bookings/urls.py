from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, PassengerViewSet

# Initialize the router
router = DefaultRouter()
router.register('flights', FlightViewSet)       # Registers endpoints for flights
router.register('passengers', PassengerViewSet) # Registers endpoints for passengers

# Define urlpatterns using the router's URLs
urlpatterns = router.urls
