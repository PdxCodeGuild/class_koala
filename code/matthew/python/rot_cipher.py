# filename: rot_cipher.py

def rot_cipher(input_string, rotation_amount):
    # a tuple of the alphabet with their indices as locations
    rot_tuple = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    cipher_string = "" # creates blank string to store encryption

    for char in input_string: # cycles through input string
        # based on input letter - finds corresponding index, moves to custom position and stores new letter into string
        # if input letter is between a - m:
        if int(rot_tuple.index(char)) < rotation_amount:
            cipher_string += rot_tuple[(int(rot_tuple.index(char)) + rotation_amount)]
        else: # if input letter is between n - z:
            cipher_string += rot_tuple[(int(rot_tuple.index(char)) - rotation_amount)]
    return cipher_string

print("") # adds a blank line separator at the start of the program

input_string = input("Please enter a word to be encrypted: ").lower() # accepts word from user / converts to lowercase
rotation_amount = int(input("Please enter the amount of rotation to be used: ")) # accepts number of movements from user / converts to an integer

# plugs inputs into function and stores result
cipher_string = rot_cipher(input_string, rotation_amount)

# prints encrypted message back to the user
print(f"The encrypted message is '{cipher_string}'.\n")
