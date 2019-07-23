import string

with open('wizard_of_oz.txt', 'r') as file:
    contents = file.read()
    translator = str.maketrans('', '', string.punctuation)
    no_puntuations = contents.translate(translator)
    no_puntuations = no_puntuations.lower().split()
    return no_puntuations

def count_words(string):
    words = []
    counts = []
    