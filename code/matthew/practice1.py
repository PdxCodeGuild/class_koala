# filename: practice1.py

# FUNDAMENTALS

# Instructions: For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.


# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 1
# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# print(is_even(35))
# print(is_even(96))


# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 2
# Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.

def opposite(a, b):
    if a >= 0 and b < 0:
        return True
    if a < 0 and b >= 0:
        return True
    else:
        return False

# print(opposite(10, -1))
# print(opposite(2, 3))
# print(opposite(-1, -1))


# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 3
# Write a function that returns True if a number within 10 of 100.

def near_100(num):
    result = abs(100 - num)
    if result < 10:
        return True
    else:
        return False

# print(near_100(50))
# print(near_100(99))
# print(near_100(105))


# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 4
# Write a function that returns the maximum of 3 parameters.

def max_of_three(a, b, c):
    if a > b and a > c:
        return(a)
    if b > a and b > c:
        return(b)
    if c > a and c > b:
        return(c)

#- OR -

def max_of_three(a, b, c):
    return max(a, b, c)

# print(max_of_three(5, 6, 2))
# print(max_of_three(-4, 3, 10))
# print(max_of_three(72.12, -34.12, 41.9))


# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 5
# Print out the powers of 2 from 2^0 to 2^20

def powers_of_two():
    for i in range(21):
        print(2 ** i)

powers_of_two()


# - - - - - - - - - - - - - - - - - - - - - - - - - -
