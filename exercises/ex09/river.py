"""File to define River class."""

__author__ = "730578942"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """This is a River. It's attributes are the days past and how many bears and fish it holds."""
    day: int
    bears: list[int]
    fish: list[int]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove fish and bears from population once they get too old."""
        bears_list: list[Bear] = []
        fish_list: list[Fish] = []
        for i in self.fish:
            if i.age < 4:
                fish_list.append(i)
        for i in self.bears:
            if i.age < 6:
                bears_list.append(i)
        self.fish = fish_list
        self.bears = bears_list
        return None
    
    def remove_fish(self, amount: int):
        """Removes fish once they are eaten."""
        self.fish = self.fish[amount:]
        return None

    def bears_eating(self):
        """Increases a bear's hunger score and decreases fish, once they are eaten."""
        for i in self.bears:
            if len(self.fish) > 5:
                i.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Removes animals once they starve."""
        bears_list: list[Bear] = []
        for i in self.bears:
            if i.hunger_score < 0:
                bears_list.append(i)
        self.bears = bears_list
        return None
        
    def repopulate_fish(self):
        """Reproduces the fish population."""
        for x in range(0, ((len(self.fish) // 2) * 4)):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Reproduces the bear population."""
        for x in range(0, (len(self.bears) // 2)):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Summarizes the day, fish count, and bear count of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Allows the river simulation to run for seven days."""
        for _ in range(7):
            self.one_river_day()
        return None
            
