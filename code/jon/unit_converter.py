distance = int(input('what is the distance to convert? '))
from_unit = input('what are the input units? ').lower()
to_unit = input('what are the output units? ').lower()

if from_unit == 'ft' or from_unit == 'feet':
    feet_to_meters = float(distance /3.281)
    if to_unit == 'mi' or to_unit == 'miles':
        result = float(feet_to_meters / 1609.344)
    elif to_unit == 'm' or to_unit == 'meters':
        result = feet_to_meters
    elif to_unit == 'ft' or to_unit == 'feet':
        result = distance
    elif to_unit == 'km' or to_unit == 'kilometers':
        result = float(feet_to_meters / 3280.84)
    print (f'{distance} {from_unit} is {result} {to_unit}')

elif from_unit == 'm' or from_unit == 'meter':
    if to_unit == 'mi' or to_unit == 'miles':
        result = float(distance / 1609.344)
    elif to_unit == 'm' or to_unit == 'meters':
        result = distance
    elif to_unit == 'ft' or to_unit == 'feet':
        result = float(distance * 3.281)
    elif to_unit == 'km' or to_unit == 'kilometers':
        result = float(distance / 1000)
    print (f'{distance} {from_unit} is {result} {to_unit}')

elif from_unit == 'km' or from_unit == 'kilometers':
    kilometers_to_meters = float(distance * 1000)
    if to_unit == 'mi' or to_unit == 'miles':
        result = float(kilometers_to_meters / 1609.344)
    elif to_unit == 'm' or to_unit == 'meters':
        result = kilometers_to_meters
    elif to_unit == 'ft' or to_unit == 'feet':
        result = float(kilometers_to_meters * 3.281)
    elif to_unit == 'km' or to_unit == 'kilometers':
        result = distance
    print (f'{distance} {from_unit} is {result} {to_unit}')

elif from_unit == 'mi' or from_unit == 'miles':
    miles_to_meters = float(distance * 1609.34)
    if to_unit == 'mi' or to_unit == 'miles':
        result = distance
    elif to_unit == 'm' or to_unit == 'meters':
        result = miles_to_meters
    elif to_unit == 'ft' or to_unit == 'feet':
        result = float(miles_to_meters * 3.281)
    elif to_unit == 'km' or to_unit == 'kilometers':
        result = float(miles_to_meters / 1000)
    print (f'{distance} {from_unit} is {result} {to_unit}')
