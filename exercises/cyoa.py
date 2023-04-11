"""EX06 - Create Your Own Adventure."""

__author__ = "730578942"

from random import randint

points: int = 0
player: str = ""

BELL_PEPPER: str = "\U0001FAD1"
BEANS: str = "\U0001FAD8"
TOMATO: str = "\U0001F345"
ONION: str = "\U0001F9C5"
CLAM: str = "\U0001F41A"


def greet() -> None:
    """Player enters their name and this function greets them."""
    global player
    print("Welcome, this quiz will determine what type of soup you are.")
    player = input("What's your name: ")


def random_questions() -> None:
    """Assigns points to the global points based on player's answers to random questions."""
    global points
    city: str = input("What is your favorite city? Singapore (1), Toronto (2), Rio de Janeiro (3), Moscow (4). Enter the number that corresponds with your selection.")
    if city == "1":
        points += 20
    if city == "2":
        points += 10
    if city == "3":
        points += 15
    if city == "4":
        points += 5
    ice: str = input("How much ice do you like in your water? The whole glass filled (1), a little (2), none (3), warm water (4)")
    if ice == "1":
        points += 5
    if ice == "2":
        points += 20
    if ice == "3":
        points += 25
    if ice == "4":
        points += 40
    princess: str = input("Who is your favorite Disney Princess? Rapunzel (1), Tiana (2), Elsa (3), Moana (4)")
    if princess == "1":
        points += 15
    if princess == "2":
        points += 20
    if princess == "3":
        points += 5
    if princess == "4":
        points += 35
    prehist_animal: str = input("What is your favorite prehistoric animal? T-rex (1), Wooly Mamooth (2), Megalodon (3), Apatosaurus (4), Saber-toothed Tiger (5)")
    if prehist_animal == "1":
        points += 30
    if prehist_animal == "2":
        points += 0
    if prehist_animal == "3":
        points += 35
    if prehist_animal == "4":
        points += 25
    if prehist_animal == "5":
        points += 15
    ultimate_question: str = input("Waffles (1) or pancakes (2)?")
    if ultimate_question == "1":
        if randint(1, 2) == 2:
            points += 10
    if ultimate_question == "2":
        if randint(1, 10) == 7:
            points += 20


def food_questions() -> None:
    """Assigns points to the global points based on player's answers to food-related questions."""
    global points
    vegetable: str = input("What is your least favorite of the following vegetables? Potato (1), Onion (2), Tomato (3), Carrot (4), Bell Pepper (5). Enter the number that corresponds with your selection.")
    if vegetable == "1":
        points += 10
    if vegetable == "2":
        points += 20
    if vegetable == "3":
        points += 30
    if vegetable == "4":
        points += 40
    if vegetable == "5":
        points += 60
    spicy: str = input("What's your spice tolerance? None (1), Medium (2), I eat carolina reapers for breakfast (3).")
    if spicy == "1":
        points += 10
    if spicy == "2":
        points += 20
    if spicy == "3":
        points += 30
    flavor: str = input("What's your favorite flavor? Salty (1), Sweet (2), Bitter (3), Sour (4), Umami (5)")
    if flavor == "1":
        points += 40
    if flavor == "2":
        points += 30
    if flavor == "3":
        points += 10
    if flavor == "4":
        points += 20
    if flavor == "5":
        points += 50


def soup(pts: int) -> str:
    """This function will return the player's soup type."""
    if pts > 120:
        return print(f"Welcome to New England! You're Clam Chowder {CLAM}.")
    elif pts > 90:
        return print(f"Bonjour! You're a bowl of French Onion Soup {ONION}.")
    elif pts > 60:
        return print(f"Get cozy! You're a nice cup of Creamy Tomato Soup {TOMATO}.")
    elif pts > 30:
        return print(f"Mamma Mia! You're a fantasic swirling bowl of Minestrone soup {BEANS}.")
    elif pts > 0:
        return print(f"Brrrr! You're best served cold as a bowl of Gazpacho {BELL_PEPPER}.")


def main() -> None:
    """This will begin the quiz."""
    global points
    idx = 0
    greet()
    quiz_type: str = input("If you want to answer random questions enter \"1\", if you want to answer food-related questions enter \"2\", if you want to exit enter \"3\"")
    while idx < 1:
        if quiz_type == "1":
            points = 0
            random_questions()
            print(soup(points))
            print(f"Your Total Quiz Points so far: {points}")
            quiz_type = input("If you want to keep answering random questions enter \"1\", if you want to switch to food-related questions enter \"2\", if you want to exit enter \"3\"")
        if quiz_type == "2":
            points = 0
            food_questions()
            print(soup(points))
            print(f"Your Total Quiz Points so far: {points}")
            quiz_type = input("If you want to switch to answering random questions enter \"1\", if you want to stay with food-related questions enter \"2\", if you want to exit enter \"3\"")
        if quiz_type == "3":
            print(f"Hope that was fun {player}! You got a total of {points} soup quiz points!")
            idx = 1
    print(f"Thanks again for playing {player}, and come back whenever you ever want to test your soupness again.")


if __name__ == "__main__":
    main()