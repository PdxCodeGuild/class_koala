jackalopes = [0, 0] # sets starting point to two jacks, aged zero
years = 0 # starting point is year zero
while len(jackalopes) < 1000: # keeps going until there's 1,000 jacks
    viable = [] # list of mating age
    for jacks in jackalopes: # checks ages in the jacks list
        if jacks >= 4 and jacks <= 8: # if within mating range, adds the age to the new viable list
            viable.append(age)
    for jackalope in viable: # checks the viable list and adds a newborn for each one
        jackalopes.append(0)
    age = 0
    while age < len(jackalopes):
        if jackalopes[age] > 9:
            jackalopes.remove(jackalopes[age])
        else:
            jackalopes[age] += 1
        age += 1
    years += 1
    print(f"{jackalopes}")

print(f"{years}")
