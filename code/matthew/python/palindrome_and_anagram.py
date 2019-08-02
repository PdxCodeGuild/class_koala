# filename: palindrome_and_anagram.py


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# PALINDROME CHECKER

print("\n***** PALINDROME CHECKER *****")

def check_palindrome(s):
    s = s.lower() # converts to lowercase
    s_reversed = s[::-1] # reverse slices string and stores it
    if s == s_reversed: # compares original to reversed
        return f"'{word}' is a palindrome." # True statement
    else:
        return f"'{word}' is not a palindrome." # False statement

word = input("Enter a word: ") # accepts input from user
print(check_palindrome(word)) # plugs input into function and prints


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# ANAGRAM CHECKER

print("\n***** ANAGRAM CHECKER *****")

def check_anagram(word1, word2):
    original1 = word1 # safeguards original input for later use
    word1 = word1.lower() # converts first input to lowercase
    word1 = word1.replace(" ", "") # removes all blank spaces
    word1 = sorted(word1) # sorts all of the letters

    # repeats same as above, but on the second input
    original2 = word2
    word2 = word2.lower()
    word2 = word2.replace(" ", "")
    word2 = sorted(word2)

    # checks if the altered words now match
    if word1 == word2:
        # True statement
        return f"'{original1}' and '{original2}' are anagrams.\n"
    else:
        # False statement
        return f"'{original1}' and '{original2}' are not anagrams.\n"

word1 = input("Enter the first word: ") # accepts 1st input
word2 = input("Enter the second word: ") # accepts 2nd input
print(check_anagram(word1, word2)) # plugs inputs into function and prints


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
