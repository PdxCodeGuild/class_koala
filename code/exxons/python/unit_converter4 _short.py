

user_distance = input('please input the distance you would like converted: ' )
units_input = input ('what are the input units (mi , ft , m , km , in or yd)? ')
units_output = input ('what are the output units (mi , ft , m , km , in or yd)? ')
#units_output = float(units_output)
#units_input = float(units_input)
user_distance = float(user_distance)

#units_list = ['ft , mi , km , m , yd , in']

#response_ft = user_distance * 0.3048
#response_mi = user_distance * 1609.34
#response_km = user_distance * 1000
#response_m = user_distance
#response_yd = user_distance / 1.0936
#response_in = user_distance * 0.0254


# inputs
if units_input == 'ft':
    m = user_distance * 0.3048
elif units_input == 'mi':
    m = user_distance * 1609.34
elif units_input == 'km':
    m = user_distance * 1000
elif units_input == 'm':
    m = user_distance / 1000
elif units_input == 'yd':
    m = user_distance / 1.0936
elif units_input == 'in':
    m = user_distance * 0.0254




# outputs
if units_output == 'ft':
    final_distance = m / 0.3048
elif units_output == 'mi':
    final_distance = m / 1609.34
elif units_output == 'km':
    final_distance = m / 1000
elif units_output == 'm':
    final_distance = m * 1000
elif units_output == 'yd':
    final_distance = m * 1.0936
elif units_output == 'in':
    final_distance = m / 0.0254



print(f'your input {user_distance} {units_input} is: {final_distance} {units_output}' )
