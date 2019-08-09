# filename: hangman.py
import random

with open('english.txt', 'r') as file:
    text = file.read().rstrip().split("\n")

def load_words(text):
    long_list = []
    for word in text:
        if len(word) > 5:
            long_list.append(word)
    return long_list

long_list = load_words(text)
random_word = random.choice(long_list)
print(random_word)

print("\nWelcome to Hangman!\n")
count = 10
while count > 0:
    guess = input("Guess a letter: ")
    for letter in random_word:
        if guess == letter:
            print(f"{letter} ", end="")
        else:
            print("_ ", end="")
    print(f"\n# of guesses remaining: {count}")
    count -= 1
