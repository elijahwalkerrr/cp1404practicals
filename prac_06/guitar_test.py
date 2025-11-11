"""Time Estimate: 40mins"""
from prac_06.guitar import Guitar

def main():
    """ Test guitar class functions"""
    g1 = Guitar("Gibson L-5 CES", 16035.40, 1925)
    g2 = Guitar("Another Guitar", 1200.00, 2013)

    print(f"{g1.name} get_age(): Expected 100. Got {g1.get_age()} ")
    print(f"{g2.name} get_age(): Expected 12. Got {g2.get_age()} ")
    print(f"{g1.name} is_vintage(): Expected True. Got {g1.is_vintage()} ")
    print(f"{g2.name} is_vintage(): Expected False. Got {g2.is_vintage()} ")

main()