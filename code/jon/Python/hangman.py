import random

# Loads list of words, turns 
def load_words(path):
    with open(path, 'r') as f:
        contents = f.read() 
        wordList = contents.split('\n')
        print(wordList)
        i = 0
        approved = []
        while i < len(wordList) -1 :
            if len(wordList[i]) > 5:
                approved.append(wordList[i])
                i += 1
            else:
                i += 1
    return approved 

def pick_word(content):
    word = random.choice(content)
    print(type(word))
    return word


def display_board():
    winning_word = (pick_word(load_words('english.txt')))
    print(f'The winning word is: {winning_word}')
    print('_ ' * len(winning_word))

# print(pick_word(load_words('english.txt')))
display_board()