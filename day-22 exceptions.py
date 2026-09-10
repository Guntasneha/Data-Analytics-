'''
==========DAY-22==========


---------------EXCEPTION HANDLING----------------

---> This is the way of handling errors.
---> we can write any number exception for one code written at try block.

try
---> the try block where we can write code whiich may contain errors.
syntax :-
    try:
       code lines
    
except
---> this will handle error that are raised at try block.
Syntax:-
  expect ErrorName:
  
try: 
    print(5/0)
    print(num)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
    
else
---> the else block will only execute, if no error at try block.

try: 
    print('hello')
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
else:
    print('no error')

finally
---> This block will execute regardless with the error at try block.

try: 
    print('hello')
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
else:
    print('no error')
finally:
    print('end')


-------------FILE HANDLING-------------------

* the file handler is a object ,which is used to create, update, read and delete.

modes of file handling/
-------------

1. read(r):- the (r) mode is used when the read() function is used

with open('hello sneha,.txt','r') as file:
    print(file.read(5))

2. write(w):-

with open('hello sneha,.txt','w') as file:
    file.write('this is sneha, i am trainee at codegnan')

3. append(a):- 
with open('hello sneha,.txt','a') as file:
    file.write('this is sneha,i am trainee at codegnan')


4. x
with open('hello sneha,.txt','x') as file:
    file.write('this is sneha,i am trainee at codegnan')



'''

