# filename: number_to_phrase.py

# imports the conversion dictionaries
from number_to_phrase_dicts import *

print("\nWelcome!\n")

roman = input("Would you like to convert a number into roman numerals? (y or n) ").lower()

# if above is "y", converts to roman numerals / if not, moves to conversion into words
if roman == "y" or roman == "yes":
    roman_input = input("\nPlease enter a number (1 - 999): ")
    # if number is not within the valid range, prints error message and quits
    if int(roman_input) < 1 or int(roman_input) > 999:
        print("\nError! Valid number not received. Exiting...\n")
        quit()

    # packs number into a tuple to be analyzed per digit placeholder
    roman_tuple = tuple(roman_input)

    # creates a custom print message for later use
    message = (f"\nThe number {roman_input} in roman numerals is")

    # if number is between 100 - 999, performs the below:
    if len(roman_tuple) == 3:
        roman_hundreds_digit, roman_tens_digit, roman_ones_digit = roman_tuple
        if roman_tens_digit == "0" and roman_ones_digit == "0":
            print(message, roman_hundreds_table[roman_hundreds_digit])
        elif roman_tens_digit != "0" and roman_ones_digit == "0":
            print(message, roman_hundreds_table[roman_hundreds_digit] + "" + roman_tens_table[roman_tens_digit])
        elif roman_tens_digit == "0" and roman_ones_digit != "0":
            print(message, roman_hundreds_table[roman_hundreds_digit] + "" + roman_ones_table[roman_ones_digit])
        else:
            print(message, roman_hundreds_table[roman_hundreds_digit] + "" + roman_tens_table[roman_tens_digit] + "" + roman_ones_table[roman_ones_digit])

    # if number is between 10 - 99, performs the below:
    elif len(roman_tuple) == 2:
        roman_tens_digit, roman_ones_digit = roman_tuple
        if roman_ones_digit == "0":
            print(message, roman_tens_table[roman_tens_digit])
        else:
            print(message, roman_tens_table[roman_tens_digit] + "" + roman_ones_table[roman_ones_digit])

    # if number is between 1 - 9, performs the below:
    else:
        roman_ones_digit = roman_input
        print(message, roman_ones_table[roman_ones_digit])

    print("\nGoodbye!\n")

# conversion to words / only activated if option for roman numerals is skipped
else:
    print("\nOkay! Let's convert a number into words instead!\n")
    num_input = input("Please enter a number (0 - 999): ")

    # prints error message and quits if number is not within the valid range
    if int(num_input) < 0 or int(num_input) > 999:
        print("\nError! Valid number not received. Exiting...\n")
        quit()

    # packs number into a tuple to be analyzed per digit placeholder
    num_tuple = tuple(num_input)

    # creates a custom print message for later use
    message = (f"\nThe number {num_input} reads as:")

    # if number is between 100 - 999, performs the below:
    if len(num_tuple) == 3:
        hundreds_digit, tens_digit, ones_digit = num_tuple
        if tens_digit == "0" and ones_digit == "0":
            print(message, hundreds_table[hundreds_digit])
        elif tens_digit == "0" and ones_digit != "0":
            print(message, hundreds_table[hundreds_digit] + " and " + ones_table[ones_digit])
        elif tens_digit == "1" and ones_digit != "0":
            print(message, hundreds_table[hundreds_digit] + " and " + teens_table[ones_digit])
        elif tens_digit != "0" and ones_digit == "0":
            print(message, hundreds_table[hundreds_digit] + " and " + tens_table[tens_digit])
        else:
            print(message, hundreds_table[hundreds_digit], tens_table[tens_digit] + "-" + ones_table[ones_digit])

    # if number is between 10 - 99, performs the below:
    elif len(num_tuple) == 2:
        tens_digit, ones_digit = num_tuple
        if ones_digit == "0":
            print(message, tens_table[tens_digit])
        elif tens_digit == "1" and ones_digit != "0":
            print(message, teens_table[ones_digit])
        else:
            print(message, tens_table[tens_digit] + "-" + ones_table[ones_digit])

    # if number is between 0 - 9, performs the below:
    else:
        ones_digit = num_input
        print(message, ones_table[ones_digit])

    print("\nGoodbye!\n")
