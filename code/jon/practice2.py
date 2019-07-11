#Problem 1

# def double_letters(x):
    
#     string_to_letters = ''
#     for i in x:
#         string_to_letters += i * 2
#     return string_to_letters

# print(double_letters('hello'))
# print(double_letters('goodbye'))

#Problem 2

# def missing_char(word):
#     new_list = []
#     for i in range(len(word)):
#         missing_letter_word = word.replace(word[i], '', 1)
#         new_list.append(missing_letter_word)

#     return(new_list)

# print(missing_char('kitten'))

#Problem 3

# def latest_letter(word):

#     # Empty highest letter since we don't know what it is yet
#     highest_letter = ''

#     # Goes through every letter in the word
#     for i in range(len(word)):

#         # Checks to see if the current highest letter is still the latest one
#         if word[i] > highest_letter:
#             highest_letter = word[i]
    
#     # Returns the highest letter
#     return highest_letter

# print(latest_letter('hello'))
# print(latest_letter('happy'))
# print(latest_letter('zylophone'))

#Problem 4

# def count_hi(word):

#     # Initialize a counter
#     # Checks to see if the word 'hi' is in the string
#     # Adds every instance of 'hi' it comes up to into the counter
#     # Displays the number of times 'hi' comes up (counter)
#     counter = 0
#     word = word.lower()
#     for i in range(len(word)):
#         if word[i] == 'h' and word[i+1] == 'i':
#                 counter +=1
            
#     return counter

# print(count_hi('hellohibyehihellohihihi'))
# print(count_hi('hihi'))
# print(count_hi('hihibyehiHi'))


#Problem 5

# def cat_dog(word):
    
#     # Initialze the cat and dog variables
#     cat = 0
#     dog = 0

#     # Loops through the letters to find the words Cat and Dog.  Adds 1 to the cat and dog variable when it finds the instance
#     for i in range(len(word)):
#         if word[i] == 'c' and word[i+1] == 'a' and word[i+2] == 't':
#             cat += 1
#         elif word[i] == 'd' and word[i+1] == 'o' and word[i+2] == 'g':
#             dog += 1

#     # Determines if there are the same amount of the words cat and dog.  Returns True if there are and False if not.
#     if cat == dog:
#         return True
#     return False

# print(cat_dog('catcatdogdogcatdog'))
# print(cat_dog('catdog'))
# print(cat_dog('dogcatcatdog'))


#Problem 6

# def count_letter(letter, word):
#     counter = 0
#     for i in range(len(word)):
#         if word[i] == letter:
#             counter += 1

#     return counter

# print(count_letter('s', 'united states of america'))
# print(count_letter('i', 'antidisestablishmentterianism'))
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis'))

#Problem 7

def lower_case(word):

    lowercase_word = word.lower().strip()
    return lowercase_word

print(lower_case('SUPER!'))
print(lower_case("        NANNANANANA BATMAN        "))