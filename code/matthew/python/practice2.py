# filename: practice2.py

# STRINGS

# Instructions: For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.


# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 1
# Get a string from the user, print out another string, doubling every letter.

def double_letters(string):
    for i in string:
        print(i * 2, end="")
    print("")

# double_letters("hello")


# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 2
# Write a function that takes a string, and returns a list of strings, each missing a different character.

def missing_char(string):
    string_list = []
    for letter in string:
        removed = string.replace(letter, "", 1)
        string_list.append(removed)
    return string_list

# print(missing_char("kitten"))


# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 3
# Return the letter that appears the latest in the english alphabet.

def latest_letter(string):
    new_high = string[0]
    for letter in string:
        if letter > new_high:
            new_high = letter
    return new_high

# latest = latest_letter("pneumonoultramicroscopicsilicovolcanoconiosis")
# print(f"The latest letter is {latest}.")


# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 4
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(string):
    count = 0
    for i in range(len(string)):
        if string[i] == "h" and string[i + 1] == "i":
            count += 1
    return count

# print(count_hi("hihi"))
# print(count_hi("hfegsigghigsgshifffaffiaffafhfafahifafafa"))

# - OR -

def count_hi(string):
    count = string.count("hi")
    return count

# print(count_hi("hihi"))


# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 5
# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

def cat_dog(string):
    cat_count = 0
    dog_count = 0
    for i in range(len(string)):
        if string[i] == "c" and string[i + 1] == "a" and string[i + 2] == "t":
            cat_count += 1
        if string[i] == "d" and string[i + 1] == "o" and string[i + 2] == "g":
            dog_count += 1
    if cat_count == dog_count:
        return True
    else:
        return False

# print(cat_dog('catdog'))
# print(cat_dog('catcat'))
# print(cat_dog('catdogcatdog'))

# - OR -

def cat_dog(string):
    cat_count = string.count("cat")
    dog_count = string.count("dog")
    if cat_count == dog_count:
        return True
    else:
        return False

# print(cat_dog('catdog'))
# print(cat_dog('catcat'))
# print(cat_dog('catdogcatdog'))


# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 6
# Return the number of letter occurances in a string.

def count_letter(letter, word):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

# print(count_letter('i', 'antidisestablishmentterianism'))
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis'))


# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Problem 7
# Convert input strings to lowercase without any surrounding whitespace.

def lower_case(string):
    lower_string = string.lower()
    stripped_string = lower_string.strip(" ")
    return stripped_string

# print(lower_case("SUPER!"))
# print(lower_case("        NANNANANANA BATMAN        "))


# - - - - - - - - - - - - - - - - - - - - - - - - - -
