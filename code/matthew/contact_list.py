# filename: contact_list.py

def load(filepath):
    """opens csv file and returns header and contents as dicts"""
    with open('contact_list.csv', 'r') as file:
        text = file.read().rstrip().split("\n")
    students = [] # empty list to hold all students
    header = text[0].split(",") # creates header list
    # cycles through each row and combines all values into a list, then zips it with header categories to form dict
    for value in range(1, len(text)): # begins one line down
        value_list = text[value].split(",")
        student = dict(zip(header, value_list))
        students.append(student)
    return header, students

def accio(students):
    """accepts first name as input and returns student record as output"""
    input_name = input("\nPlease enter the first name of the witch or wizard: ")
    for s in students:
        if s["first_name"] == input_name:
            first_name, last_name, house, year = s.get("first_name"), s.get("last_name"), s.get("house"), s.get("year")
            first_name, last_name, house = first_name.capitalize(), last_name.capitalize(), house.capitalize()
            return (f"\n{first_name} {last_name}, {house} house, Year {year}\n")

def attributes():
    """prints a list of all available student attributes"""
    print("\nFirst Name\nLast Name\nGender\nHouse\nYear\n")

# def erecto(): # creates

def help():
    """prints a glossary of terms for user reference"""
    print("\nCurrent list of available spells:")
    print("(a)ccio: to summon or 'retrieve' a student's record")
    print("(e)recto: to erect or 'create' a new student record")
    print("(o)bliviate: to erase or 'delete' a student's record")
    print("(r)eparo: to fix or 'update' a student's record")

def obliviate(students):
    """accepts first name as input and continues to delete student record"""
    input_name = input("\nPlease enter the first name of the witch or wizard: ")
    for s in students:
        if s["first_name"] == input_name:
            print(f"\nThe student record to be deleted: " +  (s.get("first_name")) + " " + (s.get("last_name")))
            confirm = input("Are you sure you wish to proceed? (y or n) ")
            if confirm == "y" or confirm == "yes":
                print("\n*** Obliviate! ***\n")
                del s # not working
                return students

def reparo():
    """accepts first name as input, allows user to select key/value to be updated and processes change accordingly"""
    input_name = input("\nPlease enter the first name of the witch or wizard: ")
    for s in students:
        if s["first_name"] == input_name:
            first_name = s.get("first_name").capitalize()
            last_name = s.get("last_name").capitalize()
            print(f"\nThe student record to be updated: {first_name} {last_name}\n")
    while True:
        print("For a list of attributes, type 'list': ")
        key = input("Which attribute would you like to update? ").lower()
        if key.startswith("li"):
            attributes()
            continue
        value = input("Which new value of the attribute would you like to set? ").lower()
        if key.startswith("f"):

        elif key.startswith("la"):
        elif key.startswith("g"):
        elif key.startswith("h"):
        elif key.startswith("y"):
        else:
            print("Not a valid option.")
            break




# welcome message
print("\nWelcome to Hogwarts School of Witchcraft and Wizardry\nDepartment of Magical Student Registration")

header, students = load("contact_list.csv")

while True:
    print("\nTo explore the list of spells, type 'help'")
    action = input("Which spell would you like to perform today? ").lower()
    if action.startswith("h"):
        help()
        continue
    elif action.startswith("a"):
        print(accio(students))
    elif action.startswith("e"):
        print(accio(students))
    elif action.startswith("r"):
        print(reparo())
    elif action.startswith("o"):
        students = obliviate(students)





    again = input("Would you like to perform another spell? (y or n) ")
    if again == "n" or again == "no":
        print("\nMischief Managed...\n")
        quit()
