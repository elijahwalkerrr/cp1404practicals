"""
Band Class for Practical 9
"""

class Band:
    """A band consisting of multiple musicians."""
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        """ Adds a musician to the band list. """
        self.musicians.append(musician)

    def __str__(self):
        """Prints the name of each member of the band"""
        return f"{self.name} ({', '.join(str(musicians) for musicians in self.musicians)})"

    def play(self):
        """Iterates through each musician and checks for instrument."""
        for musician in self.musicians:
            instrument = musician.get_instrument()
            if instrument:
                print(f"{musician.name} is playing: {instrument}")
            else:
                print(f"{musician.name} needs an instrument!")
