with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contact_list = []

header = lines.pop(0).split(",")
def make(x):
    for each in range(len(lines)-1):
        new_entry = lines.pop(0)
        new_entry = new_entry.split(',')
        contact_list.append(dict(zip(header, new_entry)))
    return contact_list
contact_list = make(contact_list)

def create(contact_list):
    name = input("Name? > ")
    fruit = input("Fruit > ")
    color = input("Color > ")
    new = []
    
    new.append(name)
    
    new.append(fruit)
    new.append(color)
    new = dict(zip(header, new))
    contact_list.append(new)
    return contact_list


def retrieve(contact_list):
    name = input("who? > ")
    for i in range(len(contact_list)):
        if contact_list[i]["name"] == name:
            return contact_list[i]


def update(contact_list):
    name = input("who? > ")
    change = input("what to change? > ")
    new = input("change to what? > ")
    for i in range(len(contact_list)):
        if contact_list[i]["name"] == name:
            which_change = contact_list[i]
            which_change[change] = new
            
    return contact_list


def delete(x):
    name = input("delete who? > ")
    for i in range(len(contact_list)-1):
        if contact_list[i]["name"] == name:
            contact_list.pop(i)
    return contact_list

def options(contact_list):
    while True:
        user = input('What would you like to do? "create", "retrieve", "update", "delete", or "finished" > ')
        if user == "finished":
            with open('contacts.csv', 'w', newline="\n") as file:
                file.write(','.join(contact_list[0].keys()))
                file.write("\n")
                for each in contact_list:
                    file.write(','.join(each.values()))
                    file.write("\n")
            break
        elif user == "create":
            create(contact_list)
        elif user == "retrieve":
            retrieve(contact_list)
        elif user == "update":
            update(contact_list)
        elif user == "delete":
            delete(contact_list)
    return contact_list

print(options(contact_list))