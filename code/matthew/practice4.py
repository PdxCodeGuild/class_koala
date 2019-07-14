# filename: practice4.py

# DICTIONARIES

# Instructions: For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 1
# Given a the two lists below, combine them into a dictionary.

def combine(fruits, prices):
    f_and_p = dict(zip(fruits, prices))
    return f_and_p

# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]

# combined = combine(fruits, prices)
# print(combined)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 2
# Using the result from the previous problem, iterate through the dictionary and calculate the average price of an item.

def average(combined):
    prices_list = list(combined.values())
    prices_summed = sum(prices_list)
    averaged = round(prices_summed / len(prices_list), 2)
    return averaged

# averaged = average(combined)
# print(averaged)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 3
# Average numbers whose keys start with the same letter. Output a dictionary containing those letters as keys and the averages.

# ONLY WORKS ON CURRENT INPUT / NEEDS UPDATING

def unify(dict):
    a_list = []
    b_list = []
    c_list = []
    dict_unify = {}
    for key in dict:
        if key.startswith("a"):
            a_list.append(dict.get(key))
            a_avg = (sum(a_list)) // len(a_list)
            dict_unify.update({"a": a_avg})
        if key.startswith("b"):
            b_list.append(dict.get(key))
            b_avg = (sum(b_list)) // len(b_list)
            dict_unify.update({"b": b_avg})
        if key.startswith("c"):
            c_list.append(dict.get(key))
            c_avg = (sum(c_list)) // len(c_list)
            dict_unify.update({"c": c_avg})
    return dict_unify

# dict = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
# print(unify(dict))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
