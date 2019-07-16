import random

def pick6():
    i = 0
    winning_numbers = []
    while i < 6:
        random_numbers = random.randint(1,99)
        winning_numbers.append(random_numbers)
        i += 1
    return(winning_numbers)

print(pick6())