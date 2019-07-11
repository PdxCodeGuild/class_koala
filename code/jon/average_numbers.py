nums = []
total = 0
while True:
    number = input('Enter a number, or \'done\': ')

    #Will calculate average if the user is done and enters 'done'    
    if number == 'done':
        print('There are ' + str(len(nums)) + ' numbers in the list.')
        for i in range(len(nums)):
            total = total + nums[i]
            average = float(total / len(nums))
        print(f'The average is:  {average}')
        break
    # Will continue to add the numbers being given into the nums list
    else:
        number2 = int(number)
        nums.append(number2)
        
        
            

    

   
        
        
        
