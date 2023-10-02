from django.test import TestCase, Client
from .models import Airport, Flight, Passenger

# Create your tests here.
class FlightTestCase(TestCase):

  def setUp(self):

    # All are dummy cases, only for tests

    # Create airports
    a1 = Airport.objects.create(code="AAA", city="City A")
    a2 = Airport.objects.create(code="BBB", city="City B")

    # Create flights
    Flight.objects.create(origin=a1, destination=a2, duration=100)
    Flight.objects.create(origin=a1, destination=a1, duration=100)
    Flight.objects.create(origin=a1, destination=a2, duration=-100)

  def test_departures_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.departures.count(), 3)

  def test_arrivals_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.arrivals.count(), 1)


  def test_valid_flight(self):
    a1 = Airport.objects.create(code="AAA", city="City A")
    a2 = Airport.objects.create(code="BBB", city="City B")
    f = Flight.objects.create(origin=a1, destination=a2, duration=100)
    self.assertTrue(f.is_valid_flight())

  def test_invalid_flight_destination(self):
    a1 = Airport.objects.create(code="AAA", city="City A")
    f = Flight.objects.create(origin=a1, destination=a1, duration=100)
    self.assertFalse(f.is_valid_flight())

  def test_invalid_flight_duration(self):
    a1 = Airport.objects.create(code="AAA", city="City A")
    a2 = Airport.objects.create(code="BBB", city="City B")
    f = Flight.objects.create(origin=a1, destination=a2, duration=-100)
    self.assertFalse(f.is_valid_flight())

  def test_flight_page_passengers(self):
    f = Flight.objects.get(pk=1)
    p = Passenger.objects.create(first="Alice", last="Adams")
    f.passengers.add(p)

    c = Client()
    response = c.get(f"/flights/{f.id}")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context["passengers"].count(), 1)
