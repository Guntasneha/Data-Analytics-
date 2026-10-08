'''

Functions --> User Defined Functions,Built-in Functions,Anonymous Functions
(lambda keyword),Recursive Function


Anonymous Functions -->Nameless Functions (Helper functions),we define them
by using lambda keyword

Syntax : lambda arg(s) : expression

#Create a function to cal the area of rectangle where length and breadth are
#7,4
def rectangle(l,b):
    """Area of rectangle"""
    return l*b
print(rectangle(7,4))
print("Area of Rectangle is",rectangle(7,4))

#Same using anonymous function

area = lambda l,b : l*b
print(area(7,4))
print(type(area))

#Find the area of square with side value as 5

area = lambda side : side**2
print(area(5))

#Social Media user login user first name last name --> full name

fname,lname = input('Enter the names').split(',')
#print(fname,lname)
full_name = lambda fname,lname : fname.title().strip()+" "+lname.title().strip()
print(full_name(fname,lname))

#accepting input from user and find even or odd

n = int(input("Enter a number:"))
result = lambda n : "Even" if n%2==0 else "Odd"
result1 = lambda n : n**2 if n%2==0 else n**3
print(result(n))
print("New Result is ",result1(n))

names = ['Codegnan','Python','Saketh','Data','Java']
g = lambda x :x in names
h = lambda x : len(x) in names #checks for len(objct) in the collection
o = lambda x : len(x)
print(g('Python'))
print(h('Codegnan'))
print(o('Saketh'))

#filter(),map(),reduce()

#filter() --> we want to specific filtered result
data = [1,3,4,5,24,12,36,3]
#filter only even numbers from list
new_data = list(filter(lambda x:x%2==0,data))
print(new_data)

#Try above using user defined function with a for loop..

def final(data):
    """Filter values"""
    new_data = []
    for i in data:
        if i % 2 == 0:
            new_data.append(i)
    return new_data
print(final(data))

#Filter desired names from the list
names = ['Saketh','Python','Akash','Neha','Sameer']
new_names = list(filter(lambda i:len(i) >=6,names))
print(new_names)

#map() --> it will apply logic for each value (Google Maps)
lst = list(map(int,input("Enter the values").split(',')))
print(lst)
data = [1,3,5,7,-23]
print(data)
final = list(map(lambda x,y:x+y,lst,data)) #it automatically maps the length
print(final)

prices = [2000,2500,1500,4500,3000]
#discount of 10% for every price
disc_prices = list(map(lambda price:(price - price *0.1),prices))
print(disc_prices)

#reduce --> functools
#reduce --> it will check for logic and make it to a single value
import functools
from functools import reduce
result = reduce(lambda x,y:x*y,[12,3,4,5,6])
print(result)
f = reduce(lambda x,y:x+y,[12,3,4,5,6])
print(f)

#Task : Try above two cases using Functions
'''

#Recursive Functions : A function can call itself
#Factorial,Fibonacci,Sum of numbers......
#Recursive Functions --> Basecase (it tells when to stop the recursion)
#                    --> Recursive case (it tells how to start recursion)

'''
def func():
    """docstring"""
    if base: #base case
        return
    func() #recursive case
func()

def test():
    """testing"""
    return test() #we missed out base case
print(test())

#let's link above case to Factorial
#5! --> 5 * (5-1) * (5-2) * (5-3) * (5-4) * 1
'''
n = int(input("Enter the value:"))
def fact(n):
    """Factorial"""
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Input must be greater than 1"
    else:
        return n * fact(n-1)
print(fact(n))

#Functions are First Class Objects 
#Function can pass another function as argument
#Fuction can return another function
#Function can be inside another function
#Function can call itself
