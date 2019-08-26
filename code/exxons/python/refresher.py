num = (0)

for i in range (0,100):
    num = num + 1

    if num % 3 == 0:
        print('Fizz')

        if num % 5 == 0:
            print('Buzz')

            if num % 3 == 0 and num % 5 == 0:
                print('FizzBuzz')
    
    else: 
        print(i)

