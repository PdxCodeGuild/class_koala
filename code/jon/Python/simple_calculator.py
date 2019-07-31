operator = input('What is the operation you would like to perform (+, -, *, /, done)? ')

while True:
    if operator == 'done':
        print('Goodbye!')
        break

    elif operator == '+':
        num1 = float(input('What is the first number? '))
        num2 = float(input('What is the second number? '))
        answer = num1 + num2
        print(f'{num1} {operator} {num2} = {answer}')
        operator = input('What is the operation you would like to perform (+, -, *, /, done)? ')

    elif operator == '-':
        num1 = float(input('What is the first number? '))
        num2 = float(input('What is the second number? '))
        answer = num1 - num2
        print(f'{num1} {operator} {num2} = {answer}')
        operator = input('What is the operation you would like to perform (+, -, *, /, done)? ')

    elif operator == '*':
        num1 = float(input('What is the first number? '))
        num2 = float(input('What is the second number? '))
        answer = num1 * num2
        print(f'{num1} {operator} {num2} = {answer}')
        operator = input('What is the operation you would like to perform (+, -, *, /, done)? ')

    elif operator == '/':
        num1 = float(input('What is the first number? '))
        num2 = float(input('What is the second number? '))
        answer = num1 / num2
        print(f'{num1} {operator} {num2} = {answer}')
        operator = input('What is the operation you would like to perform (+, -, *, /, done)? ')
