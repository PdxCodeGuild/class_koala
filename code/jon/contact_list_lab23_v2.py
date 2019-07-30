def load_list():
    with open('contactlist.csv', 'r') as file:
        lines = file.read().split() #turns all lines in the csv and it's contents into a list   
        dict_list = [] #blank list
        header = lines[0].split(',') #puts the first line of the csv into a header
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        contact = dict(zip(header, row))
        dict_list.append(contact)
    return dict_list, header

def create_contact():
    print('Excellent!  Let\'s add someone new! \n')
    new_contact = input('What is the new contacts name? ')
    new_fruit = input(f'What is {new_contact}\'s favorite fruit? ')
    new_color = input(f'What is {new_contact}\'s favorite color? ')
    new_info = '\n' + new_contact + ',' + new_fruit + ',' + new_color
    # Write new contact to CSV
    with open('contactlist.csv', 'a') as file:
        file.write(new_info)
    
# def retrieve_contact():
#     find_contact = input('Who do you think you know who is on the list (first name only? ')

    


#Main Program 

# load_list()

# print('Choose an option ')
# print(f'(c)reate a new contact? \n')
# print(f'(r)etrieve a contact? \n')
# print(f'(u)pdate a current contact? \n')
# print(f'(d)elete a user? \n')
# print(f'E(x)it? ')
# user_input = input('What would you like to do? ').lower()

# if user_input == 'x':
#     print('Thank you and have a great day!')
# elif user_input == 'c':
#     create_contact()
# elif user_input == 'r':
#     retrieve_contact()

names_list = load_list('names')
print(names)