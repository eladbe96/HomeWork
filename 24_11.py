#Question 1:
# it is recommended to use 'loop' when we want to go over all items/values in single variable, while implementing several
#tests and definitions.

#Question 2:
#The syntax of the 'for' loop is:
# for <temp variable> in <the variable we would like to examine>:
#The 'for' loop can be used for collection items.

#Question 3:
#The 'join' method is the reverse of 'split' method.
#'join' method will receive a 'character' and will create a list when each element is diveded
#by the given character.

#Question 4:
#I didnt understand the Question

#Question 5:
#I didnt understand the Question

#Question 6:
# str1 = ['eraser','table','pencil','book']
# for temp in str1:
#     print(temp[::-1])

#Question 7:
# for x in range(10,21):
#     if(x%3==0):
#         print(f'{str(x)} is divisible by 3')
#     else:
#         print(f'{str(x)} is not divisible by 3')

#Question 8:
# print one character per line:
# str2 = 'Hello world'
# for tmp in str2:
#     if(tmp != 'o'):
#         print(tmp)
#     else:
#         continue
# print all characters in single line:
# str2 = 'Hello world'
# for tmp in str2:
#     if(tmp == 'o'):
#         str2= str2.replace(tmp,"")
# print(str2)

#Question 9:
# age_list = [8,72,-35,24,56,12]
# for idx, age in enumerate(age_list):
#     if age < 0:
#         print("Error in age data")
#         break
#     else:
#         print(f'Person{str(idx+1)} is {age} years old')

#Question 10:
# ip = [192,168,10,16]
# print(str(ip).replace(",",".").replace(" ",""))



#Question 11:
# list_nums = [7,58,3,259,23]
# tmp =0
# for max in list_nums:
#     if max > tmp:
#         tmp = max
#     else:
#         continue
# print(tmp)

#Question 12:
# list_list = [[12,87,5],[-1,3000,4],[200,-8,4]]
# tmp = 0
# for x in list_list:
#     for y in x:
#         if tmp > y:
#             tmp = y
#         else:
#             continue
# print(tmp)