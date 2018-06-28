"""
ex1.py
Created by Evaldas Senavaitis
"""
import sys

fileN=input("Please enter file name:")
students=[]

def split_tuples(new_stud):
    """
    split_tuples splits all items in a file
    new_stud:is a variable for items in a file
    returns items or group of items to be used for the new ordering
    """
    new_stud=new_stud.split()
    return (new_stud[0],new_stud[1],new_stud[2],' '.join(new_stud[3:-1]),new_stud[-1],)
def print_studs(stuple):
    """
    print_studs is only joining last name with first name
    stuple: is a n from 'for' loop just as a variable
    returns a neatly looking table as it was asked in a task with right amount of spaces
    """
    full_name=stuple[4]+","+stuple[3]
    print('{:32} {:6} {:7} year {}'.format(full_name, stuple[0], stuple[2], stuple[1]))
# Trying to open a file if it fails it outputs a appropriate message
try:  
    fileName=open(fileN)
except IOError as e :
    print("Invalid input")
    sys.exit()
    
# Reads the file splits it and adds it to a list 'studens'
fileLine=fileName.read()
for new_stud in fileLine.split('\n'):
    if len(new_stud)==0:
        continue
    students.append(split_tuples(new_stud))
# Calling out a print_studs function for every item in a list to be printed out
for n in students:
    print_studs(n)  
fileName.close()
user_input = 1
# Asks user to choose by what to sort y inputing a correct number
while user_input >0:
    
    print("select what you want to choose")
    print("Type 1 to sort by degree")
    print("Type 2 to sort by regno")
    print("Type 3 to sort by year")
    print("Type 0 to exit")
    user_input=int(input("Enter a number you want to sort by: "))
    # If degree number is correct and it is in students list it will call out print_studs function
    if user_input == 1 :
        degree_num=input("By what kind of degree you want to sort:")
        for dn in students :
            if dn[2] == degree_num:
                print_studs(dn)
    # If registration number is correct and it is in students list it will call out print_studs function
    elif user_input == 2:
        reg_nr=input("What kind of registration number you want to check:")
        for rn in students:
            if rn[0] == reg_nr :
                print("*"*32)
                print(rn[3], rn[4])
                print("*"*32)
    # If there is students in supplied year gap it will call out print_studs function to be printed
    elif user_input == 3 :
        year_from=input("Type what year you want to sort from:")
        year_to=input("Type what year you want to sort to :")
        for y in students :
            if y[1]>= year_from and y[1] <= year_to:
                print_studs(y)

