"""
ass1.py
CE151 assignment 1 template
created by sands 30/10/10
modified by sands 28/10/11 - number of exercises changed
"""

def ex1() :
    """
    exercise 1
    Program counts triangle hypotenuse and finds all traingle angles
    Created by Evaldas Senavaitis 08/11/2014
    """
    print()
    from math import sqrt, atan, degrees
    width=float(input("Enter width: "))
    while width<=0 : # it will ask to input width until it is more than 0
        if width<=0 :
            width=float(input("Please enter width again which would be more than 0:"))
    height=float(input("Enter height: "))
    while height<=0 : # it will ask to input height until it is more than 0
        if height<=0 :
            height=float(input("Please enter height again which would be more than 0:"))
    hyp=(width**2)+(height**2)
    result=sqrt(hyp)
    #Degrees of width, height and hypotenuse only needed width/height and result needed
    a =(degrees(atan(width/height)))
    c =(degrees(atan(result)))
    #whole triangle angle sum is 180
    w=180
    #knowing that one angle is 90 degrees
    x=90
    #calculating third angle of triangle
    print("Knowing that one angle is 90 degrees and second one is ", format((a),'.1f'),"third angle would be ", format((w-x-a),'.1f'))
    #length of hypotenuse
    print("Hypotenuse of your inputed triangle: ",format(result, '.1f')) # displays only 1 number after dot

    
    
def ex2() :
    """
    exercise 2
    program counts fibonacci numbers and displays first n numbers 
    program created by Evaldas Senavaitis 08/11/2014
    """
    print()
    Lastn=int(input("Enter a positive integer which will display first numbers in Fibonacci series: "))
    while Lastn<=0:
        if Lastn<=0 :
            Lastn=int(input("Again please input a positive integer which will display first numbers in Fibonacci series:"))
    n=1 # n is used to turn loops one at the time
    n1=0 # n1 is used as a starting point to display first 1
    n2=1 # n2 is used to add values as loops turn.
    #print(n1, end=",") this could be used to display first as 0
    if n2>=1 : print(n2, end=",")    
    #counts fibonaci series and loops it your desired times
    while n<Lastn :
        NextNum=n1+n2
        print(NextNum, end=",")
        n1=n2
        n2=NextNum
        n=n+1
    print()
    
    
def ex3() :
    """
    exercise 3
    Program checks number is it a prime number or not
    Created by Evaldas Senavaitis 08/11/2014
    """
    print()
    n=int(input("Enter number: "))
    while n<=0:     # this loop will ask user to input integer bigger than 0
        if n<=0:
            n=int(input("Please enter again a positive integer:"))
    check=n/2 # this is used to divide n by 2
    prime=check%2 # this is used to see the remainder
    while n==1:     # this is used to loop until user input value more than 1
        if n==1:    # this if statement is writen if user input 1 
            print("The number is not prime")
            n=int(input("Please enter again which would be more than 1:"))
    if prime!=0 : # this looks if remainder is not equal to 0
        print("The number is prime")
    else :
        print("The number is not prime")
    
    
    
def ex4() :
    """
    exercise 4
    Program counts binomial coefficient of two positive integers
    Created by Evaldas Senavaitis 08/11/2014
    """
    print()
    from math import factorial # I import factorial from math just to simplyfy the task
    x=int(input("Enter x value: "))
    y=int(input("Enter y value: "))
    while y<=x :    # these statements are given is a task
        if y==1: bc=x
        if y==x: bc=1
        bc=(factorial(x))//((factorial(y)*factorial(x-y))) # this is A levels math formula for binomial coefficient 
        print(bc)
        break # break is used to cicle only 1 time, because no more than 1 is needed
    if y>x:
        bc=0
        print(bc)

    
    
def ex5() :
    """
    exercise 5
    Program inputs line of text
    Displays these words one per line
    Prints longest and shortest words
    Created by Evaldas Senavaitis 08/11/2014
    """
    print()
    MyList=str(input("Enter line of text: "))
    #MyList.capitalize() capatalizes list if needed 
    MyList=MyList.split() # thsi us used to split whole string
    MyList.sort()       # this sorts out the list
    #print('') makes spaces to program
    for e in MyList : print(e)  # for loop is used to display all words one per line
    if len(MyList)==0 : print("No text inputed")    
    def findShortest(MyList):   #def used to find shortest word in a string
        minlist = min(MyList, key=len) #using key=len and min function used to find shortest word
        return (minlist)        
    # Note than these fuction where only mentioned in week 7 lecture 
    def findLongest(MyList):    #def used to find longest word in a string
        maxlist = max(MyList, key=len)  #using key=len and max function used to find longest word
        return (maxlist)
    print("") # this is used only to make space and to look better then words are displayed one per line
    print ('Shortest word is:', findShortest(MyList))
    print ('Longest word is:', findLongest(MyList))
    
    
    
def ex6() :
    """
    exercise 6
    Counts all seperate vowels in a string and then outputs a integer as reference point to see which vowels are least occuring
    Created by Evaldas Senavaitis 08/11/2014
    """
    print()
    def find_vowels(sentence):

        """
        def finds all vowels in sentence
    
        """

        count=0
        vowels="aeiuoAEIOU"

        for letter in sentence:
            if letter in vowels:
                count += 1 #I can count whole vowels in a text if needed this is only was used for myself as a starting point
            
        a=(sentence.count("a")) # these functions counts all possible vowels in a text(sentence)
        e=(sentence.count("e"))
        i=(sentence.count("i"))
        u=(sentence.count("u"))
        o=(sentence.count("o"))
        A=(sentence.count("A"))
        E=(sentence.count("E"))
        I=(sentence.count("I"))
        O=(sentence.count("O"))
        U=(sentence.count("U"))
        a1=a+A                  # this is used to add both small and big letters and use as one
        e1=e+E
        i1=i+I
        u1=u+U
        o1=o+O
        print("a =",a1)         # this prints out all vowels in a text as a ref point for later
        print("e =",e1)
        print("i =",i1)
        print("u =",u1)
        print("o =",o1)
        lis=[]                  # opening a list to add vowels in a list
        if 0<a1<=len(MyString): # if statements below adds vowels to a list if only there is more than 0 vowels, even if a inputed text will be all 'a' letters this function would add them to a list and counts them all 
           # print("a=",a1)
            lis.append(a1)
        if 0<e1<=len(MyString):
           # print("e=",e1)
            lis.append(e1)
        if 0<i1<=len(MyString):
           # print("i=",i1)
            lis.append(i1)
        if 0<u1<=len(MyString):
           # print("u=",u1)
            lis.append(u1)
        if 0<o1<=len(MyString):
           # print("o=",o1)
             lis.append(o1)
        try:
            leastoccur=min(lis)     # this finds smallest integer in a list as a reference point to see which vowel is smallest, if there is no vowels in a inputed text it will display a message
            print("So the least accuring vowel will be a vowel which is equal to the number",leastoccur) # this is writen to display a integer as reference point for least occuring vowel
        except ValueError :
            if True:print("there is no vowels in a inputed text")
            else: print("So the least accuring vowel will be a vowel which is equal to the number",leastoccur) # this is writen to display a integer as reference point for least occuring vowel

    MyString=str(input("Enter text: "))    
    find_vowels(MyString) 

def ex7() :
    """
    exercise 7
    Created by Evaldas Senavaitis 10/11/2014
    """
    print()
    def bubblesort( lis ):
      for i in range( len( lis ) ): #in range of list lenght 
        for k in range( len( lis ) - 1, i, -1 ): # in range of list lenght and then substracting by 1 everytime looping
          if ( lis[k] < lis[k - 1] ): # if list[k] is smaller than list[k] previous swaps list positions
            swap( lis, k, k - 1 )
 
    def swap( lis, x, y ): # swaps required numbers that are smaller than upcoming numbers 
      tmp = lis[x]
      lis[x] = lis[y]
      lis[y] = tmp
        
    print("Enter non-negative integers")
    print("Use a negative to end inputing integers in a list")
    integer=int(input("First integer:"))
    lis=[]
    while integer>=0:
        lis.append(integer)
        integer=int(input("Next integer:"))
    bubblesort(lis)
    print(lis)
     
def ex8() :
    """
    exercise 8
    Created by Evaldas Senavaitis 11/11/2014
    """
    print()
    from datetime import date #imports date
    today=date.today()  #today= date then program was launched
    year=today.year     #year= year then program was launched
    FDate=input("Input date in format of dd/mm/yyyy with slashes:")
    d=int(FDate[0:2]) #takes first 2 possitions in input in integer form
    m=int(FDate[3:5]) #takes 3 and 4 possition in input in integer form
    y=int(FDate[6:10]) #takes 6 and 9 possition in input in integer form

    while d>31:   #ask to input day again if day is in wrong format
        d=int(input("Again please input correct day: "))
    while m>12:  #ask to input month again if month is in wrong format   
        m=int(input("Again please input correct month: "))
    while y<year:  #ask to input year again if year is in wrong format
        y=int(input("Again please input future year: "))
    mydate=date(y, m, d)  #makes mydate in date format for substraction available 
    TimeToDate=abs(mydate-today)  #abs is for making result possitive
    print("Days left up to your inputed date: ", TimeToDate.days) #takes only days from substraction
        
# modify the following line so that your name is displayed instead of Lisa's
print("CE151 assignment 1 - Evaldas Senavaitis")

# do not modify anything beneath this line
exlist = [None, ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8]
running = True
while running :
    line = input("Select exercise (0 to quit): ")
    if line == "0" : running = False
    elif len(line)==1 and "1"<=line<="8": exlist[int(line)]()
    else : print("Invalid input - try again")


