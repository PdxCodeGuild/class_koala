# filename: practice3.py
import random

# LISTS

# Instructions: For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 1
# Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.

def random_element(fruits):
    index = random.randint(0, ((len(fruits)) - 1))
    random_fruit = fruits[index]
    return random_fruit

# fruits = ['apples', 'bananas', 'pears']
# print(random_element(fruits))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 2
# Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.
#
# number_list = []
# while True:
#     number = input("Enter a number (or 'done'): ").lower()
#     if number == "done":
#         break
#     number_list.append(int(number))

# print(number_list)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 3
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

def eveneven(num_list):
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
    if len(even_list) % 2 == 0:
        return True
    else:
        return False

# print(eveneven([5, 6, 2]))
# print(eveneven([5, 5, 2]))

# - OR -

def eveneven(num_list):
    even_list = [num for num in num_list if num % 2 == 0]
    if len(even_list) % 2 == 0:
        return True
    else:
        return False

# print(eveneven([5, 6, 2]))
# print(eveneven([5, 5, 2]))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 4
# Print out every other element of a list, first using a while loop, then using a for loop.

def print_every_other(nums):
    new_list = []
    index = 0
    while index < len(nums):
        if index % 2 == 0:
            new_list.append(nums[index])
        index += 1
    return new_list

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(print_every_other(nums))

# - OR -

def print_every_other(nums):
    new_list = []
    index = 0
    for num in nums:
        if index % 2 == 0:
            new_list.append(num)
        index += 1
    return new_list

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(print_every_other(nums))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 5
# Write a function that returns the reverse of a list.

def reverse(nums):
    nums_reversed = nums[::-1]
    return nums_reversed

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(reverse(nums))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 6
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    new_list = [num for num in nums if num < 10]
    return new_list

# nums = [10, 1, 22, 3, 34, 5, 46, 7, 58]
# print(extract_less_than_ten(nums))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 7
# Write a function to find all common elements between two lists.

def common_elements(e1, e2):
    e3 = [e for e in e1 if e in e2]
    return e3

# e1 = ["a", "b", "c", "d", "e", 1, 2, 3, 4, 5]
# e2 = ["f", "c", "g", "e", "h", 6, 3, 7, 5, 8]
# print(common_elements(e1, e2))

# - OR -

def common_elements(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    if (set1 & set2):
        common_elements = (set1 & set2)
    else:
        common_elements = 0
    return common_elements

# nums1 = ["a", "b", "i", "d", "z", 1, 2, 13, 4, 25]
# nums2 = ["f", "c", "g", "e", "h", 6, 3, 7, 5, 8]
# print(common_elements(nums1, nums2))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 8
# Write a function to combine two lists of equal length into one, alternating elements.

def combine(e1, e2):
    e3 = []
    for i in range(len(e1)):
        e = e1.pop(0)
        e3.append(e)
        e = e2.pop(0)
        e3.append(e)
    return e3

# e1 = ['a', 'b', 'c']
# e2 = [1, 2, 3]
# print(combine(e1, e2))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 9
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number
# Optional: return a list of all pairs of numbers that sum to a target value.

def find_pair(nums, target):
    pairs = []
    nums.sort()
    for n in nums:
        test = nums.pop(0)
        for n in nums:
            if n + test == target:
                pairs.append((n, test))
        nums.append(test)
    return pairs

nums = [5, 6, 2, 3, 4]
target = 7
# print(find_pair(nums, target))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 10
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

def merge(list1, list2):
    list3 = []
    for i in range(0, len(list1)):
        list3.append([list1[i], list2[i]])
    return list3

# print(merge([5,2,1], [6,8,2])) # → [[5,6],[2,8],[1,2]]


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 11
# Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.







# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 12
# Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.







# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 13
# Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.







# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 14
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.







# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
