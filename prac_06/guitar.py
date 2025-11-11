class Guitar:
    """ Represent a Guitar Object. """
    def __init__(self, name="", cost= 0.0, year = 0):
        """ Initialise guitar attributes
            name: string, name/model of guitar
            cost: float, amount guitar worth
            year: int, year guitar made
            age: int, years since being made"""
        self.name = name
        self.cost = cost
        self.year = year
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

