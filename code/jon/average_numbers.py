nums = []
total = 0
while True:
    number = input('Enter a number, or \'done\': ')
    if number == 'done':
        print('There are ' + str(len(nums)) + ' numbers in the list.')
        for i in range(len(nums)):
            total = total + nums[i]
            average = float(total / len(nums))
        print(f'The average is:  {average}')
        break
    else:
        number2 = int(number)
        nums.append(number2)
        
        
            

    

   
        
        
        
