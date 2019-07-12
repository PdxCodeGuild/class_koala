# filename: number_to_phrase.py

# NUMBERS AS WORDS

ones_table = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}

teens_table = {"1": "eleven", "2": "twelve", "3": "thirteen", "4": "fourteen", "5": "fifteen", "6": "sixteen", "7": "seventeen", "8": "eighteen", "9": "nineteen"}

tens_table = {"1": "ten", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"}

hundreds_table = {"1": "one hundred", "2": "two hundred", "3": "three hundred", "4": "four hundred", "5": "five hundred", "6": "six hundred", "7": "seven hundred", "8": "eight hundred", "9": "nine hundred"}

# NUMBERS AS ROMAN NUMERALS

roman_ones_table = {"1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "7": "VII", "8": "VIII", "9": "IX"}

roman_tens_table = {"1": "X", "2": "XX", "3": "XXX", "4": "XL", "5": "L", "6": "LX", "7": "LXX", "8": "LXXX", "9": "XC"}

roman_hundreds_table = {"1": "C", "2": "CC", "3": "CCC", "4": "CD", "5": "D", "6": "DC", "7": "DCC", "8": "DCCC", "9": "CM"}

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
