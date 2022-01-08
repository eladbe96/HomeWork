#Question 1:
#Python supports slice notation for any sequential data type like lists, strings, tuples, bytes, bytearrays, and ranges
#We can create a new strings with specific characters we need from an existing string.
#We can duplicate an existing string with slicing as follows:
    # a='abc'
    # b=a[:]

#Question 2:
#List comprehension helps to create a new list with a shorter syntax based on the values of an existing list.
#It can be used with the values of an existing list.
#We can create the new list without the need of additional for loop, and the syntax will be shorter.

#Question 3:
#Right after the for loop that will iterate over the given list, we can add an "if" statement to specify whether
#we will add the new values to the new list based on the "if" statement.

#Question 4:

#The dictionary element is build in a format of "Key: Value".
#An entry in the dictionary is a value with a unique key.
#To make sure the keys will be unique, and wont be used twice, we can use the dictionary to ensure an additional key
#Wont be created with the same "Key" name.

#Question 5:
#In a dictionary, we cannot have 2 keys with the same name.
#In a dictionary, we can have to keys, with the same values.
#Any element,can be a value in a dictionary.

#Question 6:
# list_1 = [52,-81,35,-12,48,23,95]
# list_2 = list_1[-2::-2]

#Question 7:
# list_3 = ["I","love","to","eat","ice","cream","on","the","beach"]
# list_captile =[word.upper() for word in list_3]
# list_first = [word[0] for word in list_3]
# list_third = [word[2] for word in list_3 if len(word) >=3]
# list_length = [len(word) for word in list_3]

#Question 8:
# list_nums =[49,-1,144,64,-25,16]
# new_values =[int(num**0.5) for num in list_nums if num>0]

#Question 9:
# def KeyCheck(dictionary, value):
#     for value_test in dictionary.values():
#         if value_test == value:
#             return value_test
#         else:
#             continue
#
#     return None
#
# dict = {'Elad':25,'Merav':26,'Ima':55}
# print(KeyCheck(dict,55))

#Question 10:
# def GetSortedKeys(dictionary):
#     sorted_items = sorted(dictionary.items())
#     return sorted_items
# dict = {'elad':5,'aba': 80,'baba':23}
# print(GetSortedKeys(dict))

#Question 11:
# dict_id = {}
# ID = input("Please provide your ID:\n")
# if ID != '-1':
#     name = input("Please provide your name:\n")
#     dict_id[ID] = name
#     id_keys = dict_id.keys()
# while True:
#     ID = input("Please provide your ID:\n")
#     if ID == '-1':
#         break
#     else:
#             if ID in id_keys:
#                 print("This ID already exist")
#                 continue
#             else:
#                 name = input("Please provide your name:\n")
#                 dict_id[ID]=name
#                 id_keys = dict_id.keys()
#                 continue
#
#
# print(dict_id)


