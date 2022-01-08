
#Question 1:
# f_name = input("Please enter first name:\n")
# l_name = input("Please enter last name:\n")
# print(f'My first name is {f_name.title()} and last name is {l_name.title()}')

#Question 2:
# animal = input("Please provide animal name:\n")
# print ("The name is short") if len(animal) < 4 else print("")

#Question 3:
# tmp = "Yankee, go home"
# print(tmp.replace(',','!'))
# print(f"'e' chart exist {tmp.count('e')} times")

#Question 4:
# for x in range( 1,10):
#     if x % 2 !=0:
#         print(x)

#Question 5:
# tmp = ""
# while tmp !='Sara':
#     tmp2 = input("Please provide a name:\n")
#     if tmp2.title() == 'Sara':
#         tmp = tmp2.title()
#         print(f'We found {tmp2.title()} :)')
#     else:
#         print("This it not Sara :(")

#Question 6:
# Nums_list = [86,45,21,65,78,54,89]
####The avg of all numbers #####
# print(f"The average of all numbers the numbers in the list is {'%.2f' % ((sum(Nums_list) / (len(Nums_list))))}")
####The avg of numbers above 59 #####
# avg = 0
# count = 0
# for num in Nums_list:
#     if num > 59:
#         avg += num
#         count += 1
# print(f"The avarange of the numbers in the list is {'%.2f' % ((avg) / (count))}")

#Question 7:
# statment = input("Please provide 2 numbers divided by '+':\n")
# tmp=statment.index('+')
# print(int(statment[0:tmp])+(int(statment[(tmp+1):])))if statment[tmp-1] == " " and statment[tmp+1] == " " else print("Please add space between each chart")

#Question 8:
# statment = input("Please provide 2 numbers divided by '/':\n")
# tmp=statment.index('/')
# print("%.2f" % (int(statment[0:tmp])/(int(statment[(tmp+1):]))))if statment[tmp-1] == " " and statment[tmp+1] == " " and statment[tmp+2] != "0"  else print("Please provide valid numbers, when each chart divided by space")

#Question 9:
# while True:
#     test = input("Please provide a number:\n")
#     if test!='end':
#         sum += int(test)
#     else:
#         break
# print(sum)

#Question 10:
# time = int(input("Please provide a number present time in the day:\n"))
# if time < 5 or time > 22:
#     print ("Night")
# elif time >=5 and time <=11:
#     print ("Morning")
# elif time >=12 and time <=17:
#     print ("Day")
# elif time >=18 and time <=22:
#     print ("Evening")

#Question 11:
Full_name = "Elad Ben-David"
####Section B####
# print(Full_name[-5:])
####Section C####
# print(Full_name[:(int(len(Full_name)/3))])
####Section D####
# print(f"'a' chart exist {Full_name.count('a')} times")
####Section E####
# print (True) if Full_name.count('b') > 0 or Full_name.count('B') > 0 else print(False)
####Section F####
# Name_list = Full_name.split()
####Section G####
# Name_list = Name_list[::-1]
####Section H####
# Name_list[1] = Name_list[1].upper()
####Section I####
# Name_list[0] = Name_list[0].replace(Name_list[0][int(len(Name_list[0]) / 2)],"")
# print(Name_list)
####Section J####
# print(" ".join(Name_list))

#Question 12:
# nums_list = [5,2,-3,1000,8]
# print(f'The sum of the list is: {sum(nums_list)}')
# print(f'The smallest number is: {min(nums_list)}')
# print(f'The largest number is: {max(nums_list)}')
# print(f'The average of the list is: {(sum(nums_list))/(len(nums_list))}')
# del nums_list[2]
# print(f'The list 5 times multiplication value is: {sum(nums_list)*5}')
# del nums_list[0]
# sub_list = []
# for x in nums_list:
#     if x < (sum(nums_list))/(len(nums_list)):
#         sub_list.append(x)
# print(sub_list)

#Question 13:
min =0
max =9
count=0

while True:
    mid = (min + max) // 2
    answer = input(f'Does your number is Bigger/Smaller or Equal to {mid}?\n')
    if answer == 'Equal':
        count += 1
        break
    elif answer == 'Bigger':
        count += 1
        min = mid+1
        continue
    elif answer == 'Smaller':
        count += 1
        max = mid-1
        continue
print(f"Your number is {mid} and I found it after {count} times")