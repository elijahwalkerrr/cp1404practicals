"""Program to read all of these guitars and store them in a list of Guitar objects"""
from prac_07.guitar import Guitar


def main():
    """ Loads, sorts, prints and then adds guitars to list before """
    guitars = load_guitars("guitars.csv")
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    add_guitar(guitars)
    save_file(guitars, "guitars.csv")

def load_guitars(filename):
    """ Loads guitars file and returns guitars list"""
    with open("guitars.csv", "r") as file:
        guitars = []
        for line in file:
            parts = line.strip().split(",")
            my_guitars = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(my_guitars)
    return guitars

def add_guitar(guitars):
    """ Adds a guitar into the list using the class"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"Saved {name} ({year}) to Guitar's List")
        name = input("Name: ")

def save_file(guitars, filename):
    """ Opens and writes the new guitars list to file"""
    with open(filename, "w",) as file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=file)


main()