# Palindrome and Anagram


#Palindrome program

# def check_palindrome(word):

#     # Removes spaces in the string to make it easier to compare possible phrases
#     word2 = word.replace(' ', '')

#     # Compares if the word or phrase given is the same forward and backward
#     if word2 == word2[::-1]:
#         print(f"'{word}' is a palindrome")
#     else:
#         print(f"'{word}' is not a palindrome")

# word = input('enter a word: ').lower()

# check_palindrome(word)

# Anagram program

def check_anagram(a, b):

    # Removes spaces in the string
    word1_nospace = a.replace(' ', '')
    word2_nospace = b.replace(' ', '')

    # Sorts letters of the words
    word1_sorted = sorted(word1_nospace)
    word2_sorted = sorted(word2_nospace)

    # Checks to see if the 2 words are anagrams
    if word1_sorted == word2_sorted:
        return True
    return False

word1 = input('Enter the first word: ').lower()
word2 = input('Enter the second word: ').lower()

if check_anagram(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams")
else:
    print(f"'{word1}' and '{word2}' are not anagrams")