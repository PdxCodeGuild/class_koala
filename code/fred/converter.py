feet = float(input("What is the distance in feet?")) #User can enter distance in feet and that is stored as a variable
meters = feet*0.3048 # convert feet to meters

print("The distance in meters is: " + str(meters) + " meters") # display height in meters

units = str(input("Would you like to convert from feet, miles, kilometers, inches or yards? "))# User is able to choose what units they would like to convert from


miles = meters/1609.344 # convert miles to meters and define miles
if units == miles:
    print(float(input("What is the distance in miles?"))) #User can enter distance in miles and that is stored as a variable
    print("The distance in meters is: " + str(miles) + " meters") # display distance in meters

kilometers = meters/1000 # convert kilometers to meters
if units == kilometers:
    print(float(input("What is the distance in kilometers?"))) #User can enter distance in kilometers and that is stored as a variable
    print("The distance in meters is: " + str(kilometers) + " meters") # display distance in meters

feet = meters*3.281 # convert feet to meters
if units == feet:
    print(float(input("What is the distance in kilometers?"))) #User can enter distance in feet and that is stored as a variable
    print("The distance in meters is: " + str(kilometers) + " meters") # display distance in meters

meter = meters*1 # convert meters to meters
if units == meter:
    print(float(input("What is the distance in meters?"))) #User can enter distance in meters and that is stored as a variable
    print("The distance in meters is: " + str(meters) + " meters") # display distance in meters

inches = meters/39.37 # convert inches to meters
if units == meter:
    print(float(input("What is the distance in inches?"))) #User can enter distance in inches and that is stored as a variable
    print("The distance in meters is: " + str(inches) + " meters") # display distance in meters

yards = meters*1.094 # convert yards to meters
if units == meter:
    print(float(input("What is the distance in meters?"))) #User can enter distance in meters and that is stored as a variable
    print("The distance in meters is: " + str(yards) + " meters") # display distance in meters
