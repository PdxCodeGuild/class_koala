

user_distance = input('please input the distance you would like converted: ' )
units_input = input ('what are the input units (mi , ft , m , km , in or yd)? ')
units_output = input ('what are the output units (mi , ft , m , km , in or yd)? ')
#units_output = float(units_output)
#units_input = float(units_input)
user_distance = int(user_distance)

units_list = ['ft , mi , km , m , yd , in']

response_ft = user_distance * 0.3048
response_mi = user_distance * 1609.34
response_km = user_distance * 1000
response_m = user_distance
response_yd = user_distance / 1.0936
response_in = user_distance * 0.0254

if units_input == 'km' and units_output == 'mi':
    print (f' Your input {user_distance}km', "is:", str(response_km / 1609.34) +'mi')
elif units_input == 'ft' and units_output == 'km':
    print (f' Your input {user_distance}ft', "is:", str(response_ft / 1000) +'km')
elif units_input == 'mi' and units_output == 'km':
    print (f' Your input {user_distance}mi', "is:", str(response_mi / 1000) +'km')
elif units_input == 'km' and units_output == 'ft':
    print (f' Your input {user_distance}km', "is:", str(response_km / 0.3048) +'ft')
elif units_input == 'km' and units_output == 'm':
    print (f' Your input {user_distance}km', "is:", str(response_km) +'m')
elif units_input == 'm' and units_output == 'km':
    print (f' Your input {user_distance}m', "is:", str(response_m / 1000) +'km')
elif units_input == 'km' and units_output == 'yd':
    print (f' Your input {user_distance}km', "is:", str(response_km * 1.0936) +'yd')
elif units_input == 'yd' and units_output == 'km':
    print (f' Your input {user_distance}yd', "is:", str(response_yd / 1000) +'km')
elif units_input == 'km' and units_output == 'in':
    print (f' Your input {user_distance}km', "is:", str(response_km / 0.0254) +'in')
elif units_input == 'in' and units_output == 'km':
    print (f' Your input {user_distance}in', "is:", str(response_in / 1000) +'km')


elif units_input == 'mi' and units_output == 'ft':
    print (f' Your input {user_distance}mi', "is:", str(response_mi / 0.3048) +'ft')
elif units_input == 'mi' and units_output == 'yd':
    print (f' Your input {user_distance}mi', "is:", str(response_mi * 1.0936) +'yd')
elif units_input == 'mi' and units_output == 'in':
    print (f' Your input {user_distance}mi', "is:", str(response_mi / 0.0254) +'in')
elif units_input == 'mi' and units_output == 'm':
    print (f' Your input {user_distance}mi', "is:", str(response_mi) +'m')
elif units_input == 'ft' and units_output == 'mi':
    print (f' Your input {user_distance}ft', "is:", str(response_ft / 1609.34) +'mi')
elif units_input == 'yd' and units_output == 'mi':
    print (f' Your input {user_distance}yd', "is:", str(response_yd / 1609.34) +'mi')
elif units_input == 'in' and units_output == 'mi':
    print (f' Your input {user_distance}in', "is:", str(response_in / 1609.34) +'mi')
elif units_input == 'm' and units_output == 'mi':
    print (f' Your input {user_distance}m', "is:", str(response_m / 1609.34) +'mi')


elif units_input == 'ft' and units_output == 'yd':
    print (f' Your input {user_distance}ft', "is:", str(response_ft * 1.0936) +'yd')
elif units_input == 'ft' and units_output == 'in':
    print (f' Your input {user_distance}ft', "is:", str(response_ft / 0.0254) +'in')
elif units_input == 'ft' and units_output == 'm':
    print (f' Your input {user_distance}ft', "is:", str(response_ft) +'m')
elif units_input == 'yd' and units_output == 'ft':
    print (f' Your input {user_distance}yd', "is:", str(response_yd / 0.3048) +'ft')
elif units_input == 'in' and units_output == 'ft':
    print (f' Your input {user_distance}in', "is:", str(response_in / 0.3048) +'ft')
elif units_input == 'm' and units_output == 'ft':
    print (f' Your input {user_distance}m', "is:", str(response_m / 0.3048) +'ft')


elif units_input == 'yd' and units_output == 'in':
    print (f' Your input {user_distance}yd', "is:", str(response_yd / 0.0254) +'in')
elif units_input == 'yd' and units_output == 'm':
    print (f' Your input {user_distance}yd', "is:", str(response_yd) +'m')
elif units_input == 'in' and units_output == 'yd':
    print (f' Your input {user_distance}in', "is:", str(response_in * 1.0936) +'yd')
elif units_input == 'm' and units_output == 'yd':
    print (f' Your input {user_distance}m', "is:", str(response_m * 1.0936) +'yd')


elif units_input == 'in' and units_output == 'm':
    print (f' Your input {user_distance}in', "is:", str(response_in) +'m')
elif units_input == 'm' and units_output == 'in':
    print (f' Your input {user_distance}m', "is:", str(response_m / 0.0254) +'in')
