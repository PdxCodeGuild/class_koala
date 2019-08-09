user_feet = input(' please input the number of feet you would like converted into meters: ' )

user_feet = int(user_feet)
response = user_feet * 0.3048

#print ('if we convert your feet into meters, we get', response)

print (f' Your input {user_feet}ft', "is:", str(response) +'m')
