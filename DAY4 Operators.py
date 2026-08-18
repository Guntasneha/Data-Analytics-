DAY4 Operators

concantinations :- The + symbol will behave two ways for numeric it work normally and for other datatypes like string, list, tuple this it concatination
an = 'python'
of = 'language'
print(an + of)


Operators:- The operators are used to perform operations i9n variables and the values.
1. aithematic operator
    +, -, %, *, /, //
+ --> to add the values
num = 78
num_2 = 54
num_3 = 32
print(num+num_2)
print(num+num_3)
- ---> to subtract the values
num = 9
num_2 = 7
print(num - num_2)
* ---> to multiply
num = 8
num_2 = 4
print(num * num_2)
// ---> float devision
num = 8.6
num_2 = 4.4
print(num // num_2)
/ --> division 
num = 8
num_2 = 4
print(num / num_2)
% ---> modulus
v = 8
n = 4
print(v % n)

2. assignment operator (a=a+1 ----> a+=1)
  = , +=, -=, *=, /=, %= , //=

+= ---> is increment operator
a = 0
print(a)
a += 1
print(a)
-= ---> is decrement operator
b = 67
b -= 5
print(b)
*= ---> multiply 
c = 7
c *= 2
print(c)
%= ---> division
d = 8
d %= 4
print(d)
/= ---> mod
e = 42
e /= 12
print(e)
//= ---> float
f = 25
f //= 14
print(f)

3. comparison operator
  ==, >= , <= , >, <, !=
num = 9
num_2 = 5
print(num == num_2) # 9==5  False
print(num != num_2) # 9!=5  True
print(num < num_2)  # 9<5 
print(num > num_2)  # 9>5   
print(num <= num_2) # 9<=5
print(num >= num_2) # 9>=5

4. logical operator

And ---> if the both cases are true then it will be true 
num = 9
num_2 = 13
print(num >= num_2 and num <= 10)# 9>=13 and 9<=10
print(num <= num_2 and num >= 10)# 9<=13 and 9>=10
or ---> if the one case is true then it will be true
num = 9
num_2 = 13
print(num >= num_2 or num <= 10)
not ---> reverse of the output
num = 9
num_2 = 13
print(not(num >= num_2 or num <= 10))

5. identity operator
is 
a = [1,2]
b = [1,2]
print(id(a))
print(id(b))
print(a is b)
is not
a = [1,2]
b = [1,2]
print(id(a))
print(id(b))
print(a is not b)

6. membership operator
nums = 'python'
print('y' in nums)
print('i' not in nums)

7. bitwise operator 

