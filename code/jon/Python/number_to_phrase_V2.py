#Lab 15 Version 2

number_input = int(input('What number would you like for me to turn into a phrase?: '))

# Gets the digit in the hundreds place
hundreds_digit = (number_input // 100) % 10

# Gets the digit in the tens place
tens_digit = (number_input // 10) % 10

# Gets the digit in the ones place
ones_digit = number_input % 10

# Gets the teens
teens = ((tens_digit + ones_digit) + 10) - 1

# Dictionary of numbers and their phrases
teens_dictionary = {10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen', 20:'Twenty'}
hundreds_dictionary = {1:'One hundred', 2:'Two hundred', 3:'Three hundred', 4:'Four hundred', 5:'Five hundred', 6:'Six hundred', 7:'Seven hundred', 8:'Eight hundred', 9:'Nine hundred', 100: 'One hundred'}
tens_dictionary = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninty', 0: ''}
ones_dictionary = {0: 'Zero',  1: 'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}

# Checks for single digit number
if number_input < 10:
    print(f'{number_input} equals {ones_dictionary[number_input]}')

# Checks for 2 digit number between 10 and 19
if number_input < 20 and number_input >= 10:
    print(f'{number_input} equals {teens_dictionary[number_input]}')

# Checks for a number between 20 and 999
if number_input < 1000 and number_input >= 20:
    if hundreds_digit > 0 and tens_digit == 0 and ones_digit == 0:
        print(f'{number_input} equals {hundreds_dictionary[hundreds_digit]}')
    elif hundreds_digit > 0 and tens_digit == 0  and ones_digit <= 9:
        print(f'{number_input} equals {hundreds_dictionary[hundreds_digit]} {ones_dictionary[ones_digit]}') 
    elif hundreds_digit > 0 and tens_digit == 1 and teens < 20:
         print(f'{number_input} equals {hundreds_dictionary[hundreds_digit]} {teens_dictionary[teens]}')
    elif tens_digit <= 9 and ones_digit == 0:
         print(f'{number_input} equals {hundreds_dictionary[hundreds_digit]} {tens_dictionary[tens_digit]}')
    elif tens_digit > 0 and ones_digit > 0:
         print(f'{number_input} equals {hundreds_dictionary[hundreds_digit]} {tens_dictionary[tens_digit]} {ones_dictionary[ones_digit]}')