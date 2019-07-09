distance = int(input('what is the distance to convert into meters? '))
unit = input('what are the units? ').lower()


if unit == 'ft' or unit == 'feet':
    distance_in_meters = round((distance * 0.3048),4)
    print(f'{distance} ft is {distance_in_meters} m')

elif unit == 'mi' or unit == 'miles':
    distance_in_meters = round((distance * 1609.344),4)
    print(f'{distance} mi is {distance_in_meters} m')

elif unit == 'm' or unit == 'meters':
    print(f'{distance} m is {distance} m')

elif unit == 'km' or unit == 'kilometers':
    distance_in_meters = round((distance * 1000),4)
    print(f'{distance} km is {distance_in_meters} m')

elif unit == 'yrd' or unit == 'yards':
    distance_in_meters = round((distance / 1.094 ),4)
    print(f'{distance} yards is {distance_in_meters} m')

elif unit == 'in' or unit == 'inches':
    distance_in_meters = round((distance / 39.37),4)
    print(f'{distance} inches is {distance_in_meters} m')







