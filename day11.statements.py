'''
examples of if-else statements:
example 1:
s = 456
if s % 2 == 0:
    print('even')
else:
    print('odd')
example 2:
j = 27
if j % 27 == 0:
    print('true')
else:
    print('false')
    
.....

3. elif statements:- elif statement is used to check more possiable outcomes or more condition
example 1:
a = 90
b = 780
c = 6700
if a>b and a>c:# 90>780 and 90>6700
    print(a)
elif b>a and b>c: 780>90 and 780>6700
    print(b)
else:
    print(c)
    
example 2:
num = 2
num_2 = 3
user_opt = int(input('enter \n1.add \n2.sub \n3.mul \4.pow: '))
if user_opt == 1:
    print(num + num_2)
elif user_opt == 2:
    print(num - num_2)
elif user_opt == 3:
    print(num * num_2)
else:
    print(num ** num_2)


4. nested statements:- if inside an if statement is called as nested if.
example 
app_details = {'pin':1980}
import random
user_pass = int(input('enter your app password: '))
otp = random.randint(1000,9999)
if user_pass == app_details['pin']:
 print('password is correct')
 print(otp)
 user_otp = int(input('enter 4 digit otp: '))
 if user_otp == otp:
     print('welcome to app')
 else:
     print('incorrect otp')
else:
    print('password is incorrect')


a = int(input('enter a number: '))
if a % 2 == 0:
    print(f'{a} is even number')
else:
    print(f'{a} is odd number')

grading marks:- example
marks_ = int(input('enter your marks: '))
if marks_ >= 90:
    print('a+')
elif marks_ >= 80:
    print('a')
elif marks_ >= 70:
    print('b+')
elif marks_ >= 60:
    print('b')
elif marks_ >= 50:
    print('c+')
elif marks_ >= 40:
    print('c')
else:
    print('fail')

'''
