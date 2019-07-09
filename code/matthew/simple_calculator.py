# filename: simple_calculator.py

# used to alternate between various messages in the while loop
count = 0

print("") # adds an initial blank line separator

while True:
    if count == 0: # only run the first time through

        # asks for the operation symbol / converts to lowercase
        original_op = input("What is the operation you'd like to perform? (e.g. +, -, x or %) ").lower()

        # asks for two separate numbers to compute / converts to floats
        first_num = float(input("What is the first number? "))
        second_num = float(input("What is the second number? "))

    # only run after the first time through the loop
    if count > 0:
        original_op = None # removes initial input
        next_num = float(input("What is the next number? "))

    # checks operator and performs action accordingly
    # saves result in a new variable (1st time through), then updates result on every other time through
    if original_op == "+":
        result = first_num + second_num
    elif original_op == "-":
        result = first_num - second_num
    elif original_op == "x" or original_op == "*":
        result = first_num * second_num
    elif original_op == "%" or original_op == "/":
        result = first_num / second_num
    elif next_op == "+":
        result += next_num
    elif next_op == "-":
        result -= next_num
    elif next_op == "x" or next_op == "*":
        result *= next_num
    elif next_op == "%" or next_op == "/":
        result /= next_num

    # converts to an integer, if no decimal places
    if result % 1 == 0:
        result = int(result)
    # OR - limits or extends to two decimal places
    else:
        result = "{0:.2f}".format(result)

    if count == 0: # prints result back to user (1st time only)
        print(f"\nThe result is {result}.\n")
    if count > 0: # prints updated message (ever other time)
        print(f"\nThe new result is {result}.\n")

    # reverts back to a float for use in later operations
    result = float(result)

    # allows user to exit or enter a new operation
    next_op = input("If finished, type \"done\".\nIf you'd like to perform another operation, enter it now: ").lower()

    # exits program
    if next_op == "done":
        print("\nGoodbye!\n")
        break

    # skips original messages on next times through loop
    count += 1
