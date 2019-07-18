# filename: contact_list.py

with open('contact_list.csv', 'r') as file:
    text = file.read().rstrip().split("\n")

dict_list = [] # empty list to hold all the students
header = text[0].split(",") # creates a header list
# cycles through each row and combines all values into a list and then zips it with the header categories to form a dictionary
for value in range(1, len(text)): # begins one line down
    value_list = text[value].split(",")
    student = dict(zip(header, value_list))
    dict_list.append(student)

print(dict_list)
