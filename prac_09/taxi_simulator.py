"""
Simulator Program that uses Taxi and Silver Service Classes.
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi


def main():
    current_taxi = None
    bill = 0.0
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Lets Drive!")
    choice = input("q)uit, c)hoose taxi, d)rive")
    while choice != "q":
        if choice == "c":
            for i,taxi in enumerate(taxis):
                print(f"{i}. {taxi}")
            try:
                index = int(input("Choose taxi: "))
                current_taxi = taxis[index]
            except (ValueError, IndexError):
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("How far (km)? "))
                current_taxi.drive(distance)
                current_taxi.get_fare()
                fare = current_taxi.get_fare()
                bill += fare
        else:
            print("Invalid Choice")
        print(f"Bill To Date: ${bill}")
        choice = input("q)uit, c)hoose taxi, d)rive\n>>> ")


    for i, taxi in enumerate(taxis):
        print(f"{i}. {taxi}")
    print(f"Total Trip Cost: ${bill}")

main()
