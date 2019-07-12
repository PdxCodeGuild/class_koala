#Lab 15 Version 1

number_input = int(input('What number would you like for me to turn into a phrase?: '))

# Gets the digit in the tens place
tens_digit = number_input // 10

# Gets the digit in the ones place
ones_digit = number_input % 10

# Dictionary of numbers and their phrases
teens_dictionary = {10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen', 20:'Twenty'}
tens_dictionary = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninty'}
ones_dictionary = {1: 'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}

# Checks to see if there is single digit or double digit number
if tens_digit > 0:

    # Checks to see if the number is a -teen number and converts it
    if tens_digit > 0 and tens_digit <= 2:
        teens = teens_dictionary[number_input]
        print(f'{number_input} equals {teens}')

    # Converts double digit number that's not a -teen number
    else:    
        tens = tens_dictionary[tens_digit]
        ones = ones_dictionary[ones_digit]
        print(f'{number_input} equals {tens} {ones}')

# Converts single digit number
else:
    ones = ones_dictionary[ones_digit]
    print(f'{number_input} equals {ones}')


    

