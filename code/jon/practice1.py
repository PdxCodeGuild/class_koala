#Problem 1

# def is_even(a):
#     if a % 2 == 0:
#         return True
#     return False

# print(is_even(5))
# print(is_even(6))
# print(is_even(50))
# print(is_even(99))

#Problem 2

# def opposite(a,b):
#     if a >= 0 or b >= 0: #checks to see if a or b are positive numbers
#         if a < 0 or b < 0: #checks to see if a or b are negative
#             return True #if there is one positive and one negative
#         return False #if if both are positive
#     elif a < 0 and b < 0: #checks to see if both a and b are negative
#         return False 
          
    

# print(opposite(10, -1))
# print(opposite(2,3))
# print(opposite(-1, -1))
# print(opposite(52, -78))

#Problem 3

# def near_100(num):
#     #takes a number and checks if it is within 10 of 100
#     if abs(100 - num) <= 10: #abs to see if it's still within 10 over 100
#         return True
#     return False

# print(near_100(50))
# print(near_100(99))
# print(near_100(105))
# print(near_100(110))
# print(near_100(90))
# print(near_100(111))
# print(near_100(89))        

#Problem 4

# def maximum_of_three(a,b,c):
#     if (a >= b) and (a >= c):
#         return a
#     elif (b >= a) and (b >= c):
#         return b
#     else:
#         return c
    

# print(maximum_of_three(1,2,3))
# print(maximum_of_three(5,6,2))
# print(maximum_of_three(-4,3,10))

#Problem 5

def power_of_2(num):
    for i in range(0, num + 1):
        print (2 ** i)
        
print(power_of_2(20))