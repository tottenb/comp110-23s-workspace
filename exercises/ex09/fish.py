"""File to define Fish class."""


class Fish:
    """This is a Fish. It has age attributes."""
    
    age: int
    hunger_score = int

    def __init__(self):
        """Assigns the intial values to each attribute."""
        self.age = 0
        return None
    
    def one_day(self):
        """Changes the respective attributes after one day."""
        self.age += 1
        return None