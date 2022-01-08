#Question 1:
#We will use the 'while' loop to create an endless loop for running tests and checkes until we will reach our goal and send a 'break' command to stop the loop.

#Question 2:
#'while' loop will run until we will return a 'break' command to stop the loop.
#'do-while' will run until the condition is met according to what we have set in the while loop.

#Question 3:
# number = int(input("Please provide a number:\n"))
# tmp =1
# result =1
# while tmp - number != 1:
#     result = result * tmp
#     tmp +=1
# print (result)

#Question 4:
# num_list= [76,17,89,68,25,94]
# x = 0
# for x in num_list:
#     if x > 85:
#         print(f"{x} Very Good!")
#     elif x<59:
#         print(f"{x} Failed")
#     else:
#         print(x)

#Question 5:
# car_list=[]
# wheel =0
# while wheel >= 0:
#     wheel = int(input("How many wheels your car have?:\n"))
#     if wheel > 4:
#         print("We cannot accept your car!")
#         continue
#     elif wheel >= 0 and wheel <=4:
#         car_list.append(input("Please provide your car name:\n"))
#         continue
# print(car_list)

#Question 6:
# number = int(input("Please provide a number:\n"))
# for x in range(1,number):
#     if x%7==0:
#         print("BOOM")
#     else:
#         print(x)
