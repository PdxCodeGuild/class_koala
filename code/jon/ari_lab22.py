# Need to be able to count words
# Need to be able to count Characters
# Need to be able to count sentences
import string

# Opens file to read
with open ('gettysburg_address.txt') as f:
    contents = f.read()

# Gets the name of the file/document
name_of_file = f.name

# Counts how many words are in the document
def count_words(document):
    word_count = 0
    words = document.split()
    word_count += len(words)
    return word_count

# Counts how many characters are in the document
def count_characters(document):
    char_count = 0
    for char in document:
        if char in string.ascii_letters:
            char_count += 1
    return char_count
          
# Counts how many sentences are in the document
def count_sentences(document):
    sentences = 0
    for ending in document:
         if ending in ['.', '!', '?']:
             sentences += 1
    return sentences

# ARI scale
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# Calculates how many characters there are per word
characters_per_word = round((count_characters(contents) / count_words(contents)))

# Calculates how many words there are per sentence
words_per_sentence = round(count_words(contents) / count_sentences(contents))

# Calculates the ARI for the document
calculated_ari = round(((4.71 * (characters_per_word)) + (0.5 * (words_per_sentence)) - 21.43))

print(f'The ARI for {name_of_file} is {calculated_ari}')
print(f'This corresponds to a {(ari_scale[calculated_ari])["grade_level"]} level of difficulty')
print(f'that is suitable for an average person {(ari_scale[calculated_ari])["ages"]} years old.')
