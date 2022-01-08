#Question 1:
#A function is a specific code which only runs when we calling it.
#We can pass data via configured parameters to the function, and getting results back.

#We can create a new function using the following syntax: def <function name>(<values/parameter>):

#Question 2:
#The parameters in function are used to implement the block of code and getting the results back.
#As mentioned before, those parameters can be set by default by the function or being passed by the user.

#We can add parameters to the function, by creating them in the function, assigned default values on the function headline
#itself, or passing values to the function into the default parameters.

#We can assigned default values to the function's parameters using the following syntax: (variable='temp')
#The parameters with default values should be located in the right side of the function headline.
#Otherwise, we will get a syntax error.

#Question 3:
#When a values is being returned, we can use it for next functions and test in our original block of code.

#function returns a value using the 'return' syntax, or we can end the function with a 'print' command.

#By default, function returns a 'Boolean' value.

#Question 4:
#We can create a random number using the 'randint()' function.

#To use this function, we need to import the 'random' module.

#To use the 'random' module, we need to import the module 'random'.

#Question 5:
# def MyCheckEven(number):
#     if number%2==0:
#         return True
#     else:
#         return False
# print(MyCheckEven(4))

#Question 6:
# def MyAvarage(list):
#     result = sum(list)
#     return result/(len(list))
# print(f'The sum of your list is: {int(MyAvarage([1,4,6,8,3,7]))}')

#Question 7:
# def div(x=0,y=0):
#     return x/y
# def add(x=0,y=0):
#     return x + y
# def sub(x=0,y=0):
#     return x - y
# def mul(x=0,y=0):
#     return x * y
# x = int(input("Please provide your first number:\n"))
# y = int(input("Please provide your second number:\n"))
# print(f'The result of the multiplication is: {mul(x,y)}')
# print(f'The result of the addition is: {add(x,y)}')
# print(f'The result of the subtraction is: {sub(x,y)}')
# print(f'The result of the division is: {div(x,y)}')

#Question 8:
# def GetInRange(max,min):
#     user_num = 0
#     while user_num<min or user_num>max :
#         user_num = int(input("Please provide a number:\n"))
#     return user_num
# print(f"Your number '{GetInRange(20,5)}' is in range !")

#Question 9:
# import random
# x= random.randint(1,100)
# count= 0
# while True:
#     user_guess = int(input("Please provide your guess number from 1 to 100:\n"))
#     if user_guess > x:
#         count+=1
#         print(f"My number is lower than '{user_guess}'")
#         continue
#     elif user_guess<x:
#         count+=1
#         print(f"My number is Bigger than '{user_guess}'")
#     else:
#         count+=1
#         print(f"My number is '{user_guess}' and you find it after '{count}' guesses")