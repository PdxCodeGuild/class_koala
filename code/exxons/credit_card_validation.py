
#num_list = []


#user_cc_number = input('input your cc number please: ')

num_list = input("Please enter your cc number: ")
num_list = num_list.split(' ')

num_list = [int(i) for i in num_list]

#converts cc number to int

#user_cc_number = int(user_cc_number)
#user_cc_number = num_list.append(user_cc_number)


check_number = num_list.pop(-1)

num_list = num_list[::-1]



# only printing to make sure im on the right track and printed results show code im written does what i want
print(num_list)
print(check_number)

