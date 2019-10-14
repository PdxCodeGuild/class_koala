def cipher(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'nopqrstuvwxyzabcdefghijklm'
    encrypted = ''
    for i in range(0, len(string)):
        index_of_origin = letters.index(string[i])
        encrypted = encrypted + cipher[index_of_origin]
    return encrypted


word = input('What would you like to encrypt? ').lower()
cipher(word)
encrypted_word = cipher(word)
print(f'Original word: {word} \nEncrypted word: {encrypted_word}')