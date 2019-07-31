with open('contactlist.csv', 'r') as file:
    lines = file.read().split() #turns all lines in the csv and it's contects into a list   
    dict_list = [] #blank dictionary
    header = lines[0].split(',') #puts the first line of the csv into a header
for i in range(1, len(lines)):
    row = lines[i].split(',')
    contact = dict(zip(header, row))
    dict_list.append(contact)
print(dict_list, header)
    
