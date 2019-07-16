# Get the word from the input
# Go through each letter in the word
# Get the index number of that letter
# Find the cooresponding letter of that index in cipher
# Append that letter into an empty string
# Return the completed string

def rot_cipher(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'nopqrstuvwxyzabcdefghijklm'
    encrypted = ''
    for i in range(0, len(string)):
        index_of_origin = letters.index(string[i])
        encrypted = encrypted + cipher[index_of_origin]
    return encrypted


word = input('What word would you like to encrypt? ').lower()
rot_cipher(word)
encrypted_word = rot_cipher(word)
print(f'Original word: {word} \nEncrypted word: {encrypted_word}')





"""
    While loop version of the For loop above

    # def rot_cipher(string):
    # letters = 'abcdefghijklmnopqrstuvwxyz'
    # cipher = 'nopqrstuvwxyzabcdefghijklm'
    # i = 0
    # encrypted = ''
    # while i < len(string):
    #     index_of_origin = letters.index(string[i])
    #     encrypted = encrypted + cipher[index_of_origin]
    #     i += 1
    # return encrypted
"""