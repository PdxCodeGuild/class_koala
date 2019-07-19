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


while True:
    # stores outputs of functions into their own variables
    long_list = long_words(text)
    secret_word = random_word(long_list)

    print("\nWelcome to Hangman!\n")

    count = 10
    guessed_letters = []
    while count > 0:
        guess = input("Guess a letter: ")
        status = ""
        if guess in guessed_letters:
            print(f"\n{guess} has already been guessed.\n{current_status}\n")
            continue
        guessed_letters.append(guess)
        for letter in secret_word:
            if letter in guessed_letters:
                status += letter
            else:
                status += "_"
        if "_" not in status:
            print(f"\nYou win!\nThe word was {secret_word}\n")
            break
        if guess in secret_word:
            print(f"\nCorrect! {guess} is in the word.")
            print(status)
        if guess not in secret_word:
            count -= 1
            print(f"\nIncorrect! {guess} is not in the word.")
            print(status)
        current_status = status
        print(f"\n# of guesses remaining: {count}")
        if count == 0:
            print("You lose!\n")
            again = input("Would you like to play again? (y or n) ").lower()
            if again == "n" or again == "no":
                quit()
