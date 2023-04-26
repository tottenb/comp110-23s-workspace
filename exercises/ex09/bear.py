"""File to define Bear class."""


class Bear:
    """This is a Bear. It has age and hunger attributes."""

    age: int
    hunger_score: int

    def __init__(self):
        """Assigns the intial values to each attribute."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Changes the respective attributes after one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increases a bear's hunger score based on how many fish they eat."""
        self.hunger_score += num_fish
        return None