 Day 3: Datatypes and Typeconvertions

1. Numeric datatype:- float and integer is called a numeric datatypes

float:- A number which contains decimal value and it is called float datatype
ex:-
    price = 45.78
integer:- A normal number without any decimal value
ex:-
    num = 6789
    num_2 = 543

2. String:- String is a sequence of char that are enclosed in '',"" "", """ """
            String is immutable 
ex:-
   any_ = 'python is a language'
   all_ = "AB, @#, {[))"
    
3. List:- List is collection of different datatypes.
          and it is represent by [].that are seperated by (,)
          Inside the list we call is as the items.
          list is mutable 
ex:-
   any_ = [1,'pyuthon',[5,6]] 
   print(type(any_))

4. Tuple:- tuple is collection of different datatypes that are enclose in () and those are separated by ,(comma).
           tuple is  inmutable.
     [immutable means - can't modify
      mutable means - can modify]
ex:- 

nums = (1,89.67,'python',[3,4],(8,9))

5. Dictionary:- is the collection of key:value pairs, keys and value are separated by(:).
                key and value pair is called as a item. item is separated by(,) comma.
                Dictionary is represented using{} curly brackets.
                In keys place we can use immutable datatypes
                In values place we can use any datatype
ex:-
    data_ = {1:2,'name':'sneha', (2,3):'tuple'}
    print(data_)

integer, string, tuple these are immutable

float, 

6. sets:- is collection of unique elements and set can't allow any duplicate values inside it.it is represented by {}.and the elements are separated by (,)comma.
ex:-
   an = {1,2,2,5,6,9}
   print(an)
o/p:- 1,2,5,6,9
.......

Type convertions

float---> int, str
ex1:-
price = 45.67
print(int(price))

float-->str
price = 45.67
con = str(price)
print(type(con))

integer---> float, str
ex:-
num = 78
print(float(num))

integer-->str
ex:-
num = 78
con_ = str(num)
print(type(con_))

string---> int, float
ex:-
do = '3456'
print(int(do))

string---->float
ex:-
do = '10'
print(float(do))

list----> tuple, string
ex:-
nums = [1,2,3,4]
print(tuple(nums))

set--->list, tuple

all_ = (5,6,7)
print(list(all_))

set--->tuple
ex:-
all_ = {5,6,7}
print(tuple(all_))

dictionary--->list

details= [('name', 'sneha'),('edu', 'B.Tech')]
print(dict(details))

.....