from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Your docstring for Method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Your docstring for Method"""
        return self.__str__()

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False


class Lannister(Character):
    """Your docstring for Class"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Your docstring for Method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Your docstring for Method"""
        return self.__str__()

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Your docstring for Method"""
        return cls(first_name, is_alive)
