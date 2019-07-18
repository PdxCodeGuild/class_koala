# Need to be able to count words
# Need to be able to count Characters
# Need to be able to count sentences

# Opens file to read
with open ('/Users/techmoby43/gettysburg_address.txt') as f:
    contents = f.read()

# Counts how many words are in the document
def count_words(document):
    word_count = 0
    words = document.split()
    word_count += len(words)
    return word_count

# Counts how many characters are in the document
def count_characters(document):
    char_count = 0

      
# Counts how many sentences are in the document
def count_sentences(document):
    sentences = 0
    for ending in document:
         if ending in ['.', '!', '?']:
             sentences += 1
    return sentences

print(count_words(contents))

