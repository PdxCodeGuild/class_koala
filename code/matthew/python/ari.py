# filename: ari.py
import string # for use in the character counter

# opens file in read mode and stores as "f", reads file and stores the text in "contents"
filename = "gettsburg-address.txt" # for use in final print message
with open('gettysburg-address.txt', 'r') as f:
    contents = f.read()

# determines number of sentences by searching for common sentence separators, such as .s, !s and ?s
def sentence_counter(contents):
    sentence_total = 0
    for char in contents:
        if char in [".", "!", "?"]:
            sentence_total += 1
    return sentence_total

# determines number of words by storing each individual word into a list and then checking the length of said list
def word_counter(contents):
    word_list = contents.split()
    word_total = len(word_list)
    return word_total

# determines number of letter characters by searching the text for only valid ascii letters and storing them into a string, and then checking the length of that string
def char_counter(contents):
    char_string = ""
    for char in contents:
        if char in string.ascii_letters:
            char_string += char
    char_total = len(char_string)
    return char_total

# determines ARI by running all of the parameters through the formula. If there's a decimal place, rounds up. Converts to integer.
def ari_computer(sentences, words, characters):
    ari_float = (4.71 * (characters / words)) + (0.5 * (words / sentences)) - 21.43
    if ari_float // 1 != 0:
        ari_float += 1
    ari = int(ari_float)
    return ari

# dictionary for the potential ARI results and its correlating data
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

# stores all of the funtion results into their own variables
sentences = sentence_counter(contents)
words = word_counter(contents)
characters = char_counter(contents)
ari = ari_computer(sentences, words, characters)

# catches any result above 14 and presents same age and grade level as scores of 14
if ari > 14:
    grade = ari_scale[14].get("grade_level")
    ages = ari_scale[14].get("ages")

# matches final ARI with its respective grade level and ages
if ari in ari_scale:
    grade = ari_scale[ari].get("grade_level")
    ages = ari_scale[ari].get("ages")

# prints final results back to user
print("\n" + ("-" * 56) + "\n")
print(f"The ARI for {filename} is {ari}\nThis corresponds to a {grade} level of difficulty\nthat is suitable for an average person {ages} years old.")
print("\n" + ("-" * 56) + "\n")
