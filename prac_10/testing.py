"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def make_sentence(phrase):
    """
        Format phrase as a sentence.
        >>> make_sentence("hello")
        'Hello.'
        >>> make_sentence("It is an ex parrot.")
        'It is an ex parrot.'
        >>> make_sentence("good MORNING")
        'Good morning.'
        """
    phrase = phrase.rstrip(".")
    phrase = phrase.capitalize()
    return phrase + "."




def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail (now works)
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    assert car.fuel == 0, "Default fuel does not set correctly"

    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Pass in fuel not set correctly"

run_tests()

# Enable the docsets
doctest.testmod()
