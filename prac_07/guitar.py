class Guitar:
    """ Represent a Guitar Object. """
    def __init__(self, name="", year = 0, cost= 0.0,):
        """ Initialise guitar attributes
            name: string, name/model of guitar
            cost: float, amount guitar worth
            year: int, year guitar made
            age: int, years since being made"""
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 0

    def __str__(self):
        """Prints Guitar name, cost and year made."""
        return f"{self.name} ({self.year}) : ${self.cost}"
    def get_age(self):
        """ Returns the Guitars age in years."""
        return 2025 - self.year
    def is_vintage(self):
        """ Returns True if Guitar is 50 years or older"""
        return self.get_age() >= 50
    def __lt__(self, other):
        return self.year > other.year

