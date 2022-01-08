#Question 1 :
#The 'input' method is responsible for getting a value from a user
#By default, input returns a 'string' value.

#Question 2:
#To make the the returned value of 'input' be a integer, we have to add 'int' before the user input as below:
    #int_number = int(input("Please provide number"))
#To make the returned value of 'input' be a float, we have to add 'float' before the user input as below:
    #float_number = float(input("Please provide number"))

#Question 3:
#The 'split' method splits a string into a list, where each word is an item in the list.
#The 'split' method returns a list as the returned value.
#To make the 'split' method to split a string by other value than 'space', we have to add the splitting character between the () as below:
    #string = string.split(',') ----> In this example, the string will be split into list, divided by (,).

#Question 4:
#The 'format' method helps to format specific parts of a string.
#The main advantage of this method is when we dont know the order of the string, and we need to add values into it, when can use this method
#to add our values into the string, without taking into account the order of it.

# #Question 5:
# country = input("Please provide a country name:\n")
# capital = input("Please provide a capital city name:\n")
# print(f'The capital of {country.capitalize()} is {capital.capitalize()}')
#OR
# print("The capital of {} is {}".format(country.capitalize(),capital.capitalize()))

#Question 6:
#israel_city = input("Please provide a city name in Israel:\n")
# print(israel_city.isalpha())

#Question 7:
# color_list = ['black','red','brown','pink','grey']
# color_list.remove('pink')
# color_list.reverse()
# print(color_list)

#Question 8:
# a = "c a s a b l a n c a"
# print(a.count('a'))

#Question 9:
# num_list = [5,70,100,-20]
# num_list.remove(max(num_list))
# print(num_list)

#Question 10:
# num_list_2 = [5,9,-100,3,7,343,123]
# a = sorted(num_list_2, reverse=True)[1]
# b= num_list_2.index(a)
# num_list_2[b] = num_list_2[b]*2
# print(num_list_2)