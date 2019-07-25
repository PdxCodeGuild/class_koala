ones_dictionary = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
teens_dictionary = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty'}
tens_dictionary = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

num_to_conv = input('what number would you like to convert?: ' )
num_to_conv = int(num_to_conv)



ones_digit = num_to_conv % 10
tens_digit = num_to_conv // 10
hundredsDigit = num_to_conv //100


if tens_digit ==  0:
    if ones_digit is 0:
        print('zero')
    
    else:
        print(ones_dictionary[ones_digit]) 

if tens_digit == 1 and ones_digit <= 10:

    #print(double_digit_num)
    
    print(f'{num_to_conv} is', (teens_dictionary[num_to_conv]))


if ones_digit == 0 and tens_digit > 1 < 9:
    print(f'{num_to_conv} is', (tens_dictionary[tens_digit]))


if ones_digit > 0 and ones_digit <= 9 and tens_digit <= 9 and tens_digit > 1:
     print(f'{num_to_conv} is', (tens_dictionary[tens_digit]) + '-' + (ones_dictionary[ones_digit]))













































# if tens_digit == 1:
#     if ones_digit is 0:
#         print(tens_dictionary[10])
#     if ones_digit is 1:
#         print(tens_dictionary[11])
#     if ones_digit is 2:
#         print(tens_dictionary[12])
#     if ones_digit is 3:
#         print(tens_dictionary[13])
#     if ones_digit is 4:
#         print(tens_dictionary[14])
#     if ones_digit is 5:
#         print(tens_dictionary[15])
#     if ones_digit is 6:
#         print(tens_dictionary[16])
#     if ones_digit is 7:
#         print(tens_dictionary[17])
#     if ones_digit is 8:
#         print(tens_dictionary[18])
#     if ones_digit is 9:
#         print(tens_dictionary[19])

# if  tens_digit == 2:
#     if ones_digit is 0:
#         print(tens_dictionary[20]) 
#     if ones_digit is 1:
#         print(tens_dictionary[20] + '-'+ ones_dictionary[1])
#     if ones_digit is 2:
#         print(tens_dictionary[20] + '-' + ones_dictionary[2])
#     if ones_digit is 3:
#         print(tens_dictionary[20] + '-' + ones_dictionary[3])
    



   

