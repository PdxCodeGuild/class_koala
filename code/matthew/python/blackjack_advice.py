# filename: blackjack_advice.py
import random

# links card type to a numerical value
card_values = {
    "K": 10,
    "Q": 10,
    "J": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "A": 1
}

# links counter with written out place
counter_values = {
    1: "1st",
    2: "2nd",
    3: "3rd",
    4: "4th",
    5: "5th",
    6: "6th",
    7: "7th",
    8: "8th",
    9: "9th",
    10: "10th"
}

print("\nLet's play Blackjack!\n") # welcome message

card_list = [] # stores numerical values as we go
again = "y" # enters into while loop
counter = 1 # starts with 1st card

while True:
    card = input(f"What's your {counter_values[counter]} card? ").upper() # asks for the nth card
    # prints error message and returns to top if the received input is not a valid card type, i.e. a value in the dictionary
    if card not in card_values:
        print("\nError... Please enter a valid playing card.\n")
        continue
    card_value = card_values[card] # matches card with value
    card_list.append(card_value) # appends value to list
    card_total = sum(card_list) # totals all of the cards

    value_message = (f"\nThe value of your hand is currently {card_total}: ") # creates a custom message for later use

    # makes decision and recommendation based on hand value
    if card_total < 17:
        print(value_message, "Hit!\n")
    elif card_total < 21:
        print(value_message, "Stay!\n")
        break
    elif card_total == 21:
        print(value_message, "Blackjack!\n")
        break
    else:
        print(value_message, "BUSTED.\n")
        quit()

    counter += 1 # increases one level to next nth card


# EXTRA - allows user to check hand value vs random value
compare = input("Do you want to see how your hand would've matched up vs. the computer? (y or n) ").lower()

if compare == "y" or compare == "yes":
    computer = random.randint(17, 25) # selects a number
    compare_message = f"\nYour total: {card_total} vs. Computer: {computer}\n" # custom message for later use
    if computer > 21: # checks if computer busted
        print("\nThe computer BUSTED!\n")
    elif card_total == computer: # checks if it's a tie
        print(f"\nYou tied at {card_total}!\n")
    elif card_total > computer and card_total <= 21: # beats comp
        print(compare_message + "You win!\n")
    else: # if user scores less than computer
        print(compare_message + "You lose!\n")
else: # if user says no to earlier "compare" question
    print("\nOkay. Thanks for playing!\n")
