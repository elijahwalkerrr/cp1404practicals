"""Program to read all of these guitars and store them in a list of Guitar objects"""
from prac_07.guitar import Guitar


def main():
    guitars = load_guitars("guitars.csv")
    sort_guitars(guitars)



def load_guitars(filename):
    with open("guitars.csv", "r") as file:
        guitars = []
        for line in file:
            parts = line.strip().split(",")
            my_guitars = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(my_guitars)
    return guitars

def sort_guitars(guitars):
    guitars.sort()
    for guitar in guitars:
        print(guitar)




main()