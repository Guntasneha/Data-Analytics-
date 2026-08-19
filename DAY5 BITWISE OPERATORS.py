DAY5 BITWISE OPERATORS

Bitwise And operator
5 ---> 0101
3 --> 0010
print(5 & 3)

bitwise or
print(5 | 3)

bitwise xor
print(5 ^ 3)

>> ---> right shift
5 ---> 0101
1 ---> 0001
print(5 >> 2)

bitwise << left shift
print(5 << 1)

-----

input formatting

integer  ----> int(input())
num = int(input('enter a number: '))
print(num)

float -----> float(input())
b = float(input('enter any decimal: '))
print(b + 5)-

string ----> str(input()) or input()
jack = str(input('enter a string: '))
print('hi',jack)

list ----> 1 2 3  ---->  [1, 2, 3]
nums = list(map(int, input('enter some numbers:').split()))
print(nums)

tuple ---> 
nums = tuple(map(int, input('enter some numbers:').split()))
print(nums)

set ---> 
nums = set(map(int, input('enter some numbers:').split()))
print(nums)

eval keyword :- 
data_ = eval(input('enter number: '))
print(type(data_))

----

output formate:- 
1. seperated by comma(,)
name = 'sneha'
age = 21
print('my name is',name,'age is',age)

f string
name = sneha
age = 21
print(f'my name is {name} and i am {age} years old')

name = 'sneha'
age = 21
print('my name is %s and I am %d years old' %(name, age))

