"""
Derived Class that inherits from Car.
"""
import random

from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of a car that includes reliability attribute"""
    def __init__(self, name="", fuel=0, reliability = 0.0):
        """Initialise an unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(1,100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        else:
            distance = 0
        return distance








