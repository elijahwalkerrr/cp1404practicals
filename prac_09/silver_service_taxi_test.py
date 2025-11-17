"""
Test for silver service taxi subclass of Taxi/Car.
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    cool_taxi = SilverServiceTaxi("My Cool Taxi", 250, 2)
    cool_taxi.drive(18)
    fare = cool_taxi.get_fare()
    expected = 48.78
    assert round(fare, 2) == expected, f"Fare {fare:.2f} != {expected}"
main()
