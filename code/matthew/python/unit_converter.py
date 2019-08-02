# filename: unit_converter.py

# creates a dictionary with the units as keys and its corresponding conversion to meters as values
to_meter_table = {
    "feet": .3048,
    "miles": 1609.34,
    "meters": 1,
    "kilometers": 1000,
    "yards": .9144,
    "inches": .0254
}

# creates a dictionary with the units as keys and its corresponding conversion from meters as values
from_meter_table = {
    "feet": 3.28084,
    "miles": 0.000621371,
    "meters": 1,
    "kilometers": 0.001,
    "yards": 1.09361,
    "inches": 39.3701
}

# inserts a blank line at start of program
print("")

# asks for the distance and converts it to a floating point number
distance = float(input("What is the distance? "))

# asks for the type of measurement to input, e.g. feet, miles, etc.
input_unit = input("What are the input units? ")
# converts to lowercase
input_unit = input_unit.lower()

# checks user input for abbreviations or singular usage and converts to the relevant dictionary keys
if input_unit == "feet" or input_unit == "ft" or input_unit == "foot":
    input_unit = "feet"
elif input_unit == "miles" or input_unit == "mi" or input_unit == "mile":
    input_unit = "miles"
elif input_unit == "meters" or input_unit == "m" or input_unit == "meter":
    input_unit = "meters"
elif input_unit == "kilometers" or input_unit == "km" or input_unit == "kilometer":
    input_unit = "kilometers"
elif input_unit == "yards" or input_unit == "yrd" or input_unit == "yard":
    input_unit = "yards"
elif input_unit == "inches" or input_unit == "in" or input_unit == "inch":
    input_unit = "inches"
else: # prints the below and quits if one of the above not rec'd
    print("\nError. Requires a unit of measurement (e.g. miles, meters, feet, etc.). Exiting... \n")
    quit()

# converts input to equivalent in meters
in_meters = distance * to_meter_table[input_unit]

# asks for the type of measurement to output, e.g. feet, miles, etc.
output_unit = input("What are the output units? ")
# converts to lowercase
output_unit = output_unit.lower()

# checks user output for abbreviations or singular usage and converts to the relevant dictionary keys
if output_unit == "feet" or output_unit == "ft" or output_unit == "foot":
    output_unit = "feet"
elif output_unit == "miles" or output_unit == "mi" or output_unit == "mile":
    output_unit = "miles"
elif output_unit == "meters" or output_unit == "m" or output_unit == "meter":
    output_unit = "meters"
elif output_unit == "kilometers" or output_unit == "km" or output_unit == "kilometer":
    output_unit = "kilometers"
elif output_unit == "yards" or output_unit == "yrd" or output_unit == "yard":
    output_unit = "yards"
elif output_unit == "inches" or output_unit == "in" or output_unit == "inch":
    output_unit = "inches"
else: # prints the below and quits if one of the above not rec'd
    print("\nError. Requires a unit of measurement (e.g. miles, meters, feet, etc.). Exiting... \n")
    quit()

# converts original input to new distance type
in_units = in_meters * from_meter_table[output_unit]

# either removes decimal places if it's "essentially" a whole number or else extends / limits decimal point length to four digits
if in_units % 1 < .00001:
    in_units = int(in_units)
else:
    in_units = "{0:.4f}".format(in_units)

# removes decimal points from length if it's a whole number
if distance % 1 == 0:
    distance = int(distance)

# prints final conversion solution back to screen for the user
print(f"\n{distance} {input_unit} converts to {in_units} {output_unit}.\n")
