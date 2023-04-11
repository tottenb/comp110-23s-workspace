"""EX02 - One Shot Wordle."""

__author__ = "730578942"

secret_word: str = "python"
secret_word_length: int = len(secret_word)
guess: str = input(f"What is your {secret_word_length}-letter guess? ")
word_idx: int = 0
emoji_string: str = ""
boolean: bool = False
alt_indicies: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


while len(guess) != len(secret_word):
    guess = input(f"That was not {secret_word_length} letters! Try again: ")
if guess == secret_word:
    print(6 * GREEN_BOX)
    print("Woo! You got it!")
else:
    while word_idx < len(secret_word):
        current_letter: str = str(guess[word_idx])
        if current_letter == secret_word[word_idx]:
            emoji_string = emoji_string + GREEN_BOX
            word_idx = word_idx + 1
        else:
            while boolean is False and alt_indicies < len(secret_word):
                if current_letter == secret_word[alt_indicies]:
                    boolean = True
                else:
                    alt_indicies = alt_indicies + 1
            if boolean is True:
                emoji_string = emoji_string + YELLOW_BOX
            else:
                emoji_string = emoji_string + WHITE_BOX
            boolean = False
            word_idx = word_idx + 1
            alt_indicies = 0
    print(emoji_string)
    print("Not quite. Play again soon!")