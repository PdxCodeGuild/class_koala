nums = []

while True:
    user_choice = input('choose a number or'  ' type done if finished:')
    
    
    if user_choice == 'done':
      break 
    else: nums.append(int(user_choice))



print (nums)

total = 0
for user_choice in nums:
    total += user_choice
average = total/len(nums)
print('your average: ' + str(average))
