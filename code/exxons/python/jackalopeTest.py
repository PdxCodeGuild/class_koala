#jackalopeTest

jackalopes = [0,0]
years = 0
while len(jackalopes) < 1000:
    viable = []
    for age in jackalopes:
        if age >= 4 and age <= 8:
            viable.append(age)
    for jackalope in viable:
        jackalopes.append(0)
    i = len(jackalopes)-1
    while i >= 0:
        if jackalopes[i] > 9:
            jackalopes.remove(jackalopes[i])
        else:
            jackalopes[i] += 1
        i-=1
    years += 1
    print(f"{jackalopes}")

print(f"{years}")
