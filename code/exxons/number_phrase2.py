ones_dictionary = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
teens_dictionary = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty'}
tens_dictionary = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

num_to_conv = input('what number would you like to convert?: ' )
num_to_conv = int(num_to_conv)


hundreds_digit = num_to_conv // 100
tens_digit = num_to_conv % 100
tens_digit = tens_digit // 10
ones_digit = num_to_conv % 10


if tens_digit ==  0:
    if ones_digit is 0:
        print('zero')
    
    else:
        print(ones_dictionary[ones_digit]) 

if tens_digit == 1 and ones_digit <= 10:

    
    
    print(f'{num_to_conv} is', (teens_dictionary[num_to_conv]))


if ones_digit == 0 and tens_digit > 1 < 9:
    print(f'{num_to_conv} is', (tens_dictionary[tens_digit]))


if hundreds_digit == 0 and ones_digit > 0 and ones_digit <= 9 and tens_digit <= 9 and tens_digit > 1:
     print(f'{num_to_conv} is', (tens_dictionary[tens_digit]) + '-' + (ones_dictionary[ones_digit]))
     
if hundreds_digit > 0 and ones_digit >= 1 and tens_digit >= 1:
    print(f'{num_to_conv} is', (ones_dictionary[hundreds_digit]) + ' hundred ' + (tens_dictionary[tens_digit]) + '-' + (ones_dictionary[ones_digit]))



