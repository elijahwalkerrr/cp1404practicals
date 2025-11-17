"""
Simulator Program that uses Taxi and Silver Service Classes.
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi


def main():
    selected_taxi = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
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
            if selected_taxi:
                distance = int(input("How far (km)? "))
                selected_taxi.drive(distance)
                print(selected_taxi.get_fare())
            else:
                print("Error")


main()
