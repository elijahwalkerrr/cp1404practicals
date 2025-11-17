"""
Silver Service Taxi Class
"""
from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with a fanciness parameter."""
    flagfall = 4.5
    def __init__(self, name, fuel, fanciness = 0.0):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()
    def __str__(self):
        """Return a string like a Car but with current fare distance and flagfall"""
        return super().__str__() + f"plus flagfall of ${self.flagfall}"







