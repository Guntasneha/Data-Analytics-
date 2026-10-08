'''

Scope of the variables-->Scope is basically the region or area where the
data is accessible

Local Scope,Global Scope,Global keyword,Enclosing scope (non local keyword)
Built-in scope

#Local scope (Local variables) -->Variable(s) defined inside the function are
#accessible only

def data():
    """Local scope"""
    name = "Codegnan"
    return f'{name} is in Vizag.'
print(data())
#print(name) raises NameError 


#Global Scope -->variables defined outside the function can be accessible
#inside the function also

count = 10 #global variable
def details():
    """Global scope"""
    print(f'Value of count is {count} inside the function')
    #count = count+5 raises UnboundLocalError
details()
print(f'Value of count is {count} outside the function')

count = 10 #global variable
def details():
    """Priority of local vs global"""
    count = 15 #local variable
    print(f'Value of count is {count} inside the function')
    count = count+5 
details()
print(f'Value of count is {count} outside the functon')

#Usage of global keyword

count = 10 #global variable
def details():
    """Usageof global keyword"""
    global count
    count = count+15
    print(f'Value of count is {count} inside the function')
details()
print(f'Value of count is {count} outside the functon')

#Enclosing Scope --> Nested Functions

def outer():
    """nested functions"""
    count = 5
    def inner():
        """Inner function to use count variable"""
        #print(count)
        nonlocal count
        count = count *4
        print(f'Value of count is {count}')
    inner()
    print(f'Value of count is {count} outside')
outer()
#print(f'Value of count is {count} outside outer function')

#Built-in Scope ->Usage of built-in functions as variables

len = 13
print(len)
print(type(len)) #now you are modifying
print(len*2)

a = ['codegnan','python','data']
#print(len(a)) #raises TypeError as we have used len() somewhere

#LEBG rule -->Local,Enclosing,Built-in,Global
'''
#import this
#Built-in Functions,Anonymous Functions,Recursive Functions

#print(dir())
print(dir(__builtins__)) #returns the list of all built-ins (Functions,Errors)

#Every built-in datatype is a built-in function -->int,float,str,list,tuple,
#set,dict,bool

#print(bool('codegnan')) #returns boolean value (True)

#print(float(int(bool(24)))) #Functions as First class objects

#print(abs(-23)) #returns the absolute value
#None,'',0,False,[],(),{} -->treated as empty values
#all(),any()
x = [23,45,'poll']
x.append(None)
#print(x)
#print(all(x)) #all(iterable) it needs all values in the iterable to be exisitng

#print(any(x)) #any(iterable) it needs any one value to be present

#print(bin(12)) #bin() returns the binary value

#print(chr(67)) #returns the concerned object (char)

#print(ord('A')) #returns the ASCII value for any character,symbol

#print(),type(),len(),min(),max(),input(),range()

#print(divmod(6,2)) #perform 6//2(quotient)  --> 3 6%2(remainder) --> 0
#print(pow(4,2)) #base,exponent 
print(round(5.345))
print(round(5.346,2)) #digits to be rounded off

#filter(),map(),zip(),enumerate()
