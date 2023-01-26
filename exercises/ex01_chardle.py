"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730578942"

count: int = 0
input_word: str = input("Enter a 5-character word: ")
if len(input_word) != 5:
    print("Error: Word must contain 5 characters") 
    exit()
input_letter: str = input("Enter a single character: ")
if len(input_letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + input_letter + " in " + input_word)

if input_letter == input_word[0]:
    print(input_letter + " found at index 0")
    count = count + 1
if input_letter == input_word[1]:
    print(input_letter + " found at index 1")
    count = count + 1
if input_letter == input_word[2]:
    print(input_letter + " found at index 2")
    count = count + 1
if input_letter == input_word[3]:
    print(input_letter + " found at index 3")
    count = count + 1
if input_letter == input_word[4]:
    print(input_letter + " found at index 4")
    count = count + 1
if count == 0:
    print("No instances of " + input_letter + " found in " + input_word)
if count == 1:
    print(str(count) + " instance of " + input_letter + " found in " + input_word)
if count > 1:
    print(str(count) + " instances of " + input_letter + " found in " + input_word)
