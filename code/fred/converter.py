feet = float(input("What is the distance in feet?")) #User can enter distance in feet and that is stored as a variable
meters = feet*0.3048 # convert feet to meters

print("The distance in meters is: " + str(meters) + " meters") # display height in meters


units = str(input("Would you like to convert from feet, miles, kilometers, inches or yards? "))# User is able to choose what units they would like to convert from

if units == "feet":
    feet = float(input("What is the distane in feet?"))
    print("The distance in meters is: " + str(feet /3.281) + " meters") # display distance in meters

if units == "miles":
    miles = float(input("what is the distance in miles?"))
    print("The distance in meters is: " + str(miles *1609.344) + " meters") # display distance in meters

if units == "kilometers":
    kilometers = float(input("What is the distane in kilometers?"))
    print("The distance in meters is: " + str(kilometers * 1000) + " meters") # display distance in meters

if units == "inches":
    inches = float(input("What is the distane in inches?"))
    print("The distance in meters is: " + str(inches / 39.37) + " meters") # display distance in meters

if units == "yards":
    yards = float(input("What is the distane in yards?"))
    print("The distance in meters is: " + str(yards / 1.094) + " meters") # display distance in meters


distance = float(input("What is the distance?")) #User can enter distance with no units


input_units = str(input("Would you like to convert from feet, miles, kilometers, inches or yards? "))

if input_units == "feet":





output_units = str(input("Would you like to convert to feet, miles, kilometers, inches or yards? "))










