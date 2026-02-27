class calculator:
    """Your docstring for Class"""

    def __init__(self, vector):
        """Your docstring for Constructor"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Your docstring for Method"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Your docstring for Method"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Your docstring for Method"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Your docstring for Method"""
        if object == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
