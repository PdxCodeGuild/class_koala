# filename: hangman.py
import random

# opens file, strips whitespace, separates by newline and stores all of the words as strings into a list
with open('english.txt', 'r') as file:
    text = file.read().rstrip().split("\n")

def long_words(text):
    """extracts all words longer than five letters"""
    long_words = []
    for word in text:
        if len(word) > 5:
            long_words.append(word)
    return long_words

def random_word(long_words):
    """generates a random long word"""
    random_word = random.choice(long_words)
    return random_word

while True: # loops as long as user does not enter "n" when asked to play again
    # stores outputs of functions into their own variables
    long_list = long_words(text)
    secret_word = random_word(long_list)

    print("\nWelcome to Hangman!\n") # welcome message
    guessed_letters = [] # empty list for all letters guessed by user
    count = 10 # allows for ten guesses
    while count > 0: # loops until user runs out of guesses
        guess = input("Guess a letter: ")
        status = ""
        if guess in guessed_letters:
            print(f"\n{guess} has already been guessed.\n{current_status}\n")
            continue # allows for user to guess again w/o being penalized
        guessed_letters.append(guess)
        # builds out the status based on what has already been guessed
        for letter in secret_word:
            if letter in guessed_letters:
                status += letter
            else:
                status += "_"
        # determines that word has been completely guessed
        if "_" not in status:
            print(f"\nYou win!\nThe word was {secret_word}\n")
            again = input("Would you like to play again? (y or n) ").lower()
            if again == "n" or again == "no":
                quit()
            else:
                break
        if guess in secret_word:
            print(f"\nCorrect! {guess} is in the word.")
            print(status)
        if guess not in secret_word:
            count -= 1
            print(f"\nIncorrect! {guess} is not in the word.")
            print(status)
        current_status = status # stores a copy of status to display if the user guesses a repeat letter
        print(f"\n# of guesses remaining: {count}")
        if count == 0: # prints once user runs out of guesses
            print("You lose!\n")
            again = input("Would you like to play again? (y or n) ").lower()
            if again == "n" or again == "no":
                quit()
