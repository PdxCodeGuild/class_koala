# filename: credit_card_validation.py

def cc_validation(cc_number):
    cc_number = cc_number.replace(" ", "") # removes possible spaces
    cc_list = [] # empty list for the individual cc numbers
    for num in cc_number: # cycles through each number
        digit = int(num) # converts from string to integer
        cc_list.append(digit) # adds integer to the cc list
    check_digit = cc_list.pop() # removes last digit and stores it
    cc_list_reversed = cc_list[::-1] # reverses cc list
    cc_list_doubled = [] # empty list for the doubled cc numbers
    count_double = 0 # sets count for below for loop
    for i in cc_list_reversed: # cycles through each number
        if count_double % 2 == 0: # checks numbers position
            num_doubled = i * 2 # if every other, doubles...
            cc_list_doubled.append(num_doubled) # ... then appends
        else: # if not every other...
            cc_list_doubled.append(i) # ... appends original number
        count_double += 1 # increments to determine every other
    cc_list_subtracted = [] # empty list for the subtracted numbers
    for i in cc_list_doubled: # cycles through numbers
        if i > 9: # if number is more than nine...
            num_subtracted = i - 9 # ... subtracts nine...
            cc_list_subtracted.append(num_subtracted) # then appends
        else: # if not over nine...
            cc_list_subtracted.append(i) # ... appends original
    cc_list_summed = str(sum(cc_list_subtracted)) # sums all numbers and converts to a string
    second_digit = int(cc_list_summed[1]) # selects 2nd digit, converts to an integer and stores it
    if second_digit == check_digit: # checks vs. original last digit
        return "Valid!" # True statement
    else:
        return "Not Valid." # False statement


cc_number = input("Please enter the credit card number: ")
print(cc_validation(cc_number)) # plugs input into function / prints
