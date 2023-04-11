"""Ask user for number, give hints about if number is wrong"""

SECRET: int = 10
guess: int = int(input("Guess a number"))
playing: bool = True

while playing:
    if guess == SECRET:
        print("Correct!")
        playing = False
    else:
        if guess % 2 == 1:
            print("Your guess is odd. The answer is even.")
        if guess < SECRET:
            print("Your guess is too low.")
        if guess > SECRET:
            print("Your guess is too high.")
        guess = int(input("Wrong guess. Try again"))

    
