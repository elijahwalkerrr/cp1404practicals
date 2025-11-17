"""
Test loop for unreliable car subclass.
"""

from prac_09.unreliable_car import UnreliableCar

def main():
    my_car = UnreliableCar("Hyundai Tuscon", 200, 30)
    test_car(my_car)
    print(f"{200 - my_car.fuel} times out of 100 my car worked successfully")

def test_car(car):
    for i in range(1,100):
        car.drive(1)
main()


