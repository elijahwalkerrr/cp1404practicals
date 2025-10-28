

class ProgrammingLanguage:
    """ """
    def __init__(self, name="", typing ="", reflection=False, year=0):
        """Initialise a Programming Language
                name: string, language name
                typing: string, type of typing
                reflection: boolean
                year: int, year of language origin"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns true if the language is dynamic."""
        if self.typing.lower() == "dynamic":
            return True
        else:
            return False
    def __str__(self):
        """ Prints language name, tying, reflection and year of origin. """
        return f"{self.name}, {self.typing}, Reflection = {self.reflection}, First Appeared in {self.year}"


