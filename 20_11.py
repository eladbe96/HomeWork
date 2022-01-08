#Qeustion 1:
#1. Checking if a provided value is existing in a given variable.
#2. The 'IN' function returns a boolean value.
#3. The 'IN' function can be used with 'list' or 'strings'

#Qeustion 2:
#1. To write a condition in Python, we can use the 'if' operator as the following example: if a > b.
#2. The difference between 'elif' and 'else' is that 'elif' is another available option in regards of the first condition
# and it can be used in the middle of the 'condition' flow. However, 'else' will be used in the end of the condition flow, when there
# is no other available option.

#Qeustion 3:
#Python is using the indentation to identify if the next line is part of the condition flow.

#Qeustion 4:
# a = int(input("Please enter a number:\n"))
#print(if a%2==0)
#     print(True)
# else:
#     print(False)

# Qeustion 5:
# nums_list =input("Please provide a list of numbers diveded by ',':\n")
# nums_list=nums_list.split(',')
# if('3' in nums_list) and len(nums_list) > 5:
#     print(True)
# else:
#     print(False)

#Qeustion 6:
# word = input("Please provide a word:\n")
# print ("probably a complete action") if(word[-1] == 'd') and (word[-2] == 'e') else print("")

#Qeustion 7:
# num_1 = int(input("Please provide the first number:\n"))
# num_2 = int(input("Please provide the second number:\n"))
# num_3 = int(input("Please provide the third number:\n"))
# print(f"The biggest number is {max(num_1,num_2,num_3)}")

#Qeustion 8:
# age = float(input("Please provide your age:\n"))
# if age > 1:
#     if age >=18 and age < 60:
#         print("Adult")
#     elif age > 1 and  age < 18:
#         print("Teenager")
#     else:
#         print("Senior")
# else:
#     print("Baby")

#Qeustion 9:
# name = input("Please provide your name:\n")
# if name =="arthur" or name == "philip" or name == "peter":
#     print(f"Nice to meet you {name.capitalize()}, want to be a king")
# elif name =="einstein" or name == "tesla" or name == "bell":
#     print(f"Nice to meet you {name.capitalize()}, you must be a genius")
# else:
#     print(f"Nice to meet you {name.capitalize()}")

#Qeustion 10:
# condition = input("Please provide a numeric condition:\n")
# condition = condition.split(" ")
# tmp = (int(condition[0])) + (int(condition[2]))
# if tmp == (int(condition[-1])):
#     print(True)
# else:
#     print(False)

# #Qeustion 11:
####Subtraction####
# condition = input("Please provide a numeric condition:\n")
# condition = condition.split(" ")
# tmp = (int(condition[0])) - (int(condition[2]))
# if tmp == (int(condition[-1])):
#     print(True)
# else:
#     print(False)

####Multiplication####
# condition = input("Please provide a numeric condition:\n")
# condition = condition.split(" ")
# tmp = (int(condition[0])) * (int(condition[2]))
# if tmp == (int(condition[-1])):
#     print(True)
# else:
#     print(False)

####Division####
# condition = input("Please provide a numeric condition:\n")
# condition = condition.split(" ")
# tmp = (int(condition[0])) / (int(condition[2]))
# if tmp == (int(condition[-1])):
#     print(True)
# else:
#     print(False)
