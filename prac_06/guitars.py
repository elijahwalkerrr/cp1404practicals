from prac_06.guitar import Guitar


def main():
    """ Gets and Prints Guitars, using guitar class."""
    print("My Guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = valid_input("Year", int)
        cost = valid_input("Cost", float)
        guitar = Guitar(name,cost,year)
        print(f"{guitar} added.")
        guitars.append(guitar)
        name = input("Name: ")


    guitars.append(Guitar("Gibson L-5 CES", 16035.40, 1920 ))
    guitars.append(Guitar("Line 6 JTV-59",100.32 , 2010))

    print("These are my guitars: ")
    for i, guitar in enumerate(guitars,1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def valid_input(label, value_type):
    """ Validates User input"""
    while True:
        try:
            value = value_type(input(f"{label}: "))
            if value < 0:
                print(f"{value} must be >= 0")
            else:
                return value
        except ValueError:
            print(f"Invalid ({label} is not {value_type})")



main()
