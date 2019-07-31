# filename: average_numbers.py

counter = 0 # used to later change input message
sum_total = 0 # sets starting sum count to zero
num_list = [] # creates an empty list
repeat = True # enters into the while loop

print("") # creates a blank line at start of program

# accepts number from user and adds it to the list; when "done", breaks out of the loop
while repeat == True:
    if counter == 0: # first message
        user_number = input("Please enter a number.\nWhen finished, type \"done\": ").lower() # accepts as lowercase string
        print("") # provides a line separator
    elif counter % 4 == 0: # adds a reminder after every 3rd input
        print("") # provides a line separator
        user_number = input("Reminder: When finished, type \"done\".\nPlease enter another number: ").lower() # accepts as lowercase string
    else:
        user_number = input("Please enter another number: ").lower() # accepts as lowercase string
    if user_number == "done":
        break
    num_list.append(float(user_number)) # converts to a float in order to add it to the list as a number
    counter += 1 # used to move to alternative input messages

# iterates through custom list and adds all of the numbers together
for num in num_list:
    sum_total += num

# divides the sum of the list by its length to get the average
average = sum_total / len(num_list)

# prints message back to user - includes total numbers entered, the sum total of all of the numbers and the average - two decimal places
print("\nYou entered " + str(len(num_list)) + " numbers for a sum total of " + "{0:.2f}".format(sum_total) + ".\nThe average is " + "{0:.2f}".format(average) + ".\n")
