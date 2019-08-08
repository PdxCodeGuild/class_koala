# Credit Card Validation Program

def validate (cardnumber):

    # Turn the CC number from a string to a list of int's
    new_card_number = [int(i) for i in cardnumber]

    # Save the check digit
    check_digit = new_card_number.pop()

    # Reversing the digits
    reversed_digits = new_card_number[::-1]
  
    # Double every other element in the reversed list
    doubled_numbers = []
    i = 0
    while i <= len(reversed_digits) - 1:
        if i % 2 == 0:
            doubled_numbers.append(reversed_digits[i] * 2)
            i += 1
        else:
            doubled_numbers.append(reversed_digits[i])
            i += 1

    # Subtract 9 from numbers over 9
    minus_nine = []
    i = 0
    while i <= len(doubled_numbers) -1:
        if doubled_numbers[i] > 9:
            minus_nine.append(doubled_numbers[i] - 9)
            i += 1
        else:
            minus_nine.append(doubled_numbers[i])
            i += 1

    # Sum all Values
    sum_of_values = sum(minus_nine)

    # Checking if valid
    if (sum_of_values % 10) == check_digit:
        return True
    return False
    
card_number = input('What credit card number would you like to validate? ')

if validate(card_number) == True:
    print(f'Credit card number {card_number} is VALID!')
else:
    print(f'Credit cared number {card_number} is Not Valid')
