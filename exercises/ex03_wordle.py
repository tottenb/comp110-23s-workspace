"""EX03 - Wordle."""

__author__ = "730578942"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(string1: str, string_one_chr:str) -> bool:
    """Returns True if string_one_chr is found in string1"""
    assert len(string_one_chr) == 1
    string_idx: int = 0
    boolean: bool = False
    if string1[string_idx] == string_one_chr:
        boolean = True
    else:
        while string_idx < len(string1):
            current_letter: str = str(string1[string_idx])
            if current_letter == string_one_chr:
                boolean = True
                return boolean
            else:
                string_idx = string_idx + 1
                if string_idx == len(string1) and boolean == False:
                    boolean = False
    return boolean

def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    guess_idx: int = 0
    alt_idx: int = 0
    emoji_string: str = ""
    while guess_idx < len(secret):
        current_letter: str = str(guess[guess_idx])
        if current_letter == secret[guess_idx]:
            emoji_string = emoji_string + GREEN_BOX
            guess_idx = guess_idx + 1
        else:
            if contains_char(secret, current_letter) == True:
                emoji_string = emoji_string + YELLOW_BOX
                guess_idx = guess_idx + 1
            else:
                emoji_string = emoji_string + WHITE_BOX
                guess_idx = guess_idx + 1
    return emoji_string
            
def input_guess(expected_length: int) -> str:
    user_input: str = input(f"What is your {expected_length}-letter guess? ")
    while expected_length != len(user_input):
        user_input = input(f"That was not {expected_length} letters! Try again: ")
    return user_input

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 1
    secret_word: str = "codes"
    win: bool = False
    #guess: str = input(f"Enter a {len(codes)} character word: ")
    while turn_number < 7 and win is False:
        print(f"=== Turn {turn_number}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            win = True
            return print(f"You won in {turn_number}/6 turns!")
        else: 
            turn_number = turn_number + 1
    if win is False:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()