user_choices = []
div_choice = "/"
add_choice = "+"
mult_choice = '*'
sub_choice = '-'
user_finished = 'done'


def add_numbers(x,y):
            return x+y
            
def sub_numbers(x,y):
            return x-y

def mult_numbers(x,y):
            return x*y
            
def div_numbers(x,y):
            return x/y
            
            


    


while True:
    
    user_operation = input('what operation would you like to perform?:')    
    
    if user_operation == 'done':
        print('Goodbye')
        break
    if user_operation == '+':
        user_number = input('what is the first number?:') 
        user_number = int(user_number)
        
        user_number2 = input('what is the second number?:')
        user_number2 = int(user_number2)
        
        
        user_choices.append(int(user_number))
        user_choices.append(int(user_number2))
        
        
        sum_of_add = add_numbers(user_number,user_number2)

        print (f'{user_number} + {user_number2} = {sum_of_add}')
        
    

    if user_operation == '-':
        user_number = input('what is the first number?:') 
        user_number = int(user_number)
        
        user_number2 = input('what is the second number?:')
        user_number2 = int(user_number2)
    
        
        
        user_choices.append(int(user_number))
        user_choices.append(int(user_number2))
        
        
        sum_of_sub = sub_numbers(user_number,user_number2)

        print (f'{user_number} - {user_number2} = {sum_of_sub}')
        
   
    if user_operation == '*':
        user_number = input('what is the first number?:') 
        user_number = int(user_number)
        
        user_number2 = input('what is the second number?:')
        user_number2 = int(user_number2)
    
        
        
        user_choices.append(int(user_number))
        user_choices.append(int(user_number2))
        
        
        sum_of_mult = mult_numbers(user_number,user_number2)

        print (f'{user_number} * {user_number2} = {sum_of_mult}')
        
    
    if user_operation == '/':
        user_number = input('what is the first number?:') 
        user_number = int(user_number)
        
        user_number2 = input('what is the second number?:')
        user_number2 = int(user_number2)
    
        
        
        user_choices.append(int(user_number))
        user_choices.append(int(user_number2))
        
        
        sum_of_div = div_numbers(user_number,user_number2)

        print (f'{user_number} / {user_number2} = {sum_of_div}')