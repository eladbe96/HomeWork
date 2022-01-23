
import sqlite3
import random
from collections import Counter
connection = sqlite3.connect(r'C:\Users\user\PycharmProjects\DevOps\SQL\TestDB.db')

#Question 1 & 3:

def SpcialEntry(Name,Age,Address,Salary):
    cursor = connection.execute(f"SELECT * from Company where NAME = '{Name}'")
    for i in cursor:
        if Name == i[1]:
            Check =input(f"The name {Name} is already in the company table\nPress 'Y' to update the new entry:\nOtherwise press anything else:\n")
            if Check.capitalize() == "Y":
                connection.execute(f"update Company set AGE = {Age}, SALARY = {Salary}, ADDRESS = '{Address}' where NAME = '{Name}';")
                print(f"Entry {i[0]} was updated seccssfully!")
                printData(i[0])
                connection.commit()
                return True
            else:
                return False
        else:
            return False


def printData(ID):
    cursor = connection.execute(f"SELECT * FROM COMPANY WHERE ID = {ID}")
    for record in cursor:
        print(f"ID={record[0]}, Name={record[1]}, Age={record[2]}, Address={record[3]}, Salary={record[4]}")


def NewEntry ():
    ID = random.randint(12,999)
    Name = input("Please provide the name of the new employee:\n")
    while True:
        if Name.isalpha()==False:
            Name = input("Input can be only A-Z,a-z!\nPlease provide the name of the new employee:\n")
            continue
        else:
            if Name.capitalize()!=Name:
                Name = Name.capitalize()
                print(f"The name {Name} was capitalized!")
            break
    Age = input("Please provide the age of the new employee:\n")
    while True:
        if Age.isdigit() == False:
            Age = input("Input can be integers, between 18-67!\nPlease Please provide the age of the new employee:\n")
            continue
        else:
            if(int (Age) < 18) or (int(Age) > 67):
                Age = input("Input can be integers, between 18-67!\nPlease Please provide the age of the new employee:\n")
                continue
            else:
                break
    Salary = input("Please provide the salary of the new employee:\n")
    while True:
        if Salary.isdigit()==False:
          Salary = input("Input can be integers, between 18-67!\nPlease Please provide the salary of the new employee:\n")
          continue
        else:
            break
    Address = input("Please provide the address of the new employee:\n")
    while True:
        if (Address.replace(" ","")).isalpha()==False:
            Address = input("Input can be only A-Z,a-z!\nPlease provide the address of the new employee:\n")
            continue
        else:
            break
    if SpcialEntry(Name,Age,Address,Salary):
        None
    else:
        connection.execute(f"insert into Company values ({ID},'{Name}',{Age},'{Address}','{Salary}');")
        connection.commit()



def main():
    NewEntry()

    check_restart = input("Please enter 'Y' to add another employee:\nOtherwise press anything else:\n")
    if check_restart == 'Y':
        main()
    else:
        None


#Question 2:

def FindDup(Column):
    cursor = connection.execute(f"SELECT * from Company where {Column} = (SELECT {Column} from Company GROUP by {Column} HAVING count ({Column}) > 1)")
    print("The following entries found as duplicates under the column:")
    for i in cursor:
        print (i)
    To_Keep = int(input("Please provide the entry's ID that you would like to keep:\n"))
    # cursor_2 = connection.execute(f"delete FROM Company where ID != {To_Keep} AND (SELECT {Column} from Company GROUP by {Column} HAVING count ({Column}) > 1)")
    cursor = connection.execute(f"SELECT * from Company where {Column} = (SELECT {Column} from Company GROUP by {Column} HAVING count ({Column}) > 1)")
    for x in cursor:
        if x[0] != To_Keep:
            cursor_2 = connection.execute(f"delete from Company where ID = {x[0]}")
    connection.commit()
FindDup("AGE")


if __name__ == '__main__':
    main()