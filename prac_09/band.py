"""
Band Class for Practical 9
"""

class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        return f"{self.name} ({', '.join(str(musicians) for musicians in self.musicians)})"

    def play(self):
        for musician in self.musicians:
            instrument = musician.get_instrument()
            if instrument:
                print(f"{musician.name} is playing: {instrument}")
            else:
                print(f"{musician.name} needs an instrument!")
