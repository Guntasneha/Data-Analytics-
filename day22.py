'''
for <temp> in range(obj):
    statement(s)..


Nested Loops -->(for in for) -->These are primarily used for Pattern printings,
Matrix operations and problems solving scenarios (data structures)..

Syntax:

for i in range(outer_loop_range):
    for j in range(inner_loop_range): #inner loop will be completely executed
                                     #for every outer loop
        #code block 

for i in range(3): #i -->0,1,2
    for j in range(2):#j -->0,1
        print(f'i = {i},j = {j}')
      
#In above case for complete j value of 0 i value wil be 0,1,2 and follows
#same for others

for i in range(3): #in this case both i and j are same
    for j in range(3):
        print(i,j)

for i in range(3):
    for j in range(3):
        print(i,j,end=' ') #now entire result will be in one single line
        print("python")
    #print('Codegnan')
    print() #only when inner loop is complete before starting outer
            #loop it generates

for i in range(2): #i ->0,1
    for j in range(i): #first i value will be 0 loop doesnt start for j
        print(f'i = {i},j={j}')
for i in range(3):
    for j in range(i+1):
        print(f'i = {i},j={j}')

for i in range(3):
    for j in range(i-1): #as here for i=0,j becomes -ve,i =1 j becomes 0
        print(f'i={i},j={j}')


#now lets link above to patterns

#Square pattern

for i in range(3):
    for j in range(3):
        print('*',end=' ') #check here by changing end argment
    print()

#Rectangle pattern

* * * *
* * * *
* * * *

#same as square pattern we just change inner loop
for i in range(3):
    for j in range(4):
        print('*',end=' ')
    print()

#Number based patterns -->Row wised,Column wised...

1 2 3 4
1 2 3 4
1 2 3 4

for i in range(3): #i --> 0,1,2
    for j in range(4): #j-->0,1,2,3
        print(j+1,end=' ')
    print()

#now keeping both start and end values
for i in range(1,4):
    for j in range(1,5):
        print(j,end=' ')
    print()

1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4

#outer loop determines number of rows
#inner loop determines number of columns

for i in range(1,5):
    for j in range(1,5):
        print(i,end=' ')
    print()

1 2 3
4 5 6
7 8 9

#for above number grid lets take square pattern as example
num = 1
for i in range(3):
    for j in range(3):
        print(num,end=' ') #check here by changing end argment
        num+=1
    print()


'''

Nested Loops --> Pattern problems -->Square,Rectangle,Number Grid,Number patterns

Right Angled Triangle Pattern

*
* *
* * *
* * * *
* * * * *

for i in range(5):
    for j in range(i+1):
        #print(f'i = {i},j={j}')
        print('*',end=' ')
    print()

Inverted Triangle Pattern

* * * * *
* * * *
* * *
* *
*

for i in range(5):
    for j in range(5-i):
        #print(f'i = {i},j={j}')
        print('*',end=' ')
    print()

Star Pyramid Pattern

    *
   * *
  * * *
 * * * *
* * * * *

#Lets assume we take number of rows
rows = 5
for i in range(1,rows+1):
    #print spaces
    for j in range(rows-i):
        print(" ",end='')
    #print stars
    for j in range(i):
        print('*',end=' ')
    print()

Floyd's Triangle Pattern

1
2 3
4 5 6
7 8 9 10

num = 1
for i in range(4):
    for j in range(i+1):
        #print(f'i = {i},j={j}')
        print(num,end=' ')
        num=num+1
    print()

Tasks:
A
B C
D E F
G H I J

A
B B
C C C
D D D D

0
1 1
2 2 2
3 3 3 3
4 4 4 4

#Specialcase -->Diamond Pattern Start Pyramid combine with inverted star pyramid
'''

#Datatypes,Operators,Control Block,Exception Handling,File Handling

#Procedure Oriented Programming -> Functions --> A Function is a block
#of code that performs a specific task,we have keyword def
#User defined Functions,Built-in Functions,Anonymous Functions,Recursive
#Functions
'''
Syntax:

def fname(parameters): #functn defn
    """Doc String(describe your function)"""
    statement(s)...
    .......                #body of function
    .......
    return value(s)....
fname(args) #function call
  
def intro():
    """Intro to Functions"""
    #return "Hope you are learning and enjoying the journey"
    return "Hope you are learning and enjoying the journey","hey hai"
print(intro())

#Positional Arguments,Keyword Arguments,Default arguments,
#Variable length arguments,Keyword Variable length arguments

def add(a,b):
    """Simple addition function"""
    return a+b
print(add(5,7)) #Addition
print(add('codegnan','python')) #concatenation
print(add([1,2,3],[8,9,89])) #merging
c,d = map(int,input("Enter the values").split(','))
print(add(c,d))
#print(add(9,8,9,4)) raises TypeError as positional arguments didnot match

#Positional Arguments -->order of arguments in function definition and
#function call should match

#Keyword Arguments -->name of the arguments should match

def grocery(item,price):
    """Keyword arguments usage"""
    print(f'Item is {item}')
    print(f'Price is {price}')
grocery("Milk",35)
print(grocery(price=45,item="Bread")) #it also returns None as nothing to be
                                     #printed
#grocery("Jam",100,2) #in this case Positional arguments fails as we have only
#2 arguments in function definition
'''
#Default arguments -->we can make any number of arguments as default
#but we have a thumbrule -->only first argument cannot be default
#non default arguments follows default arguments

#def grocery(item,price=30):
#def grocery(item="Milk",price): raises Error
def grocery(item="jam",price=50):
    """Keyword arguments usage"""
    print(f'Item is {item}')
    print(f'Price is {price}')
grocery("Milk",35)
grocery("Bread")
grocery()






















