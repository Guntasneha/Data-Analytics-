'''
def prime(num=10,count = 1):
    for j in range(1,num+1):
        if num % j == 0:
            count += 1
            print(count)
    if count == 2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')


def data_(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data_(name='sneha',age=21,location='vizag',batch=6)
......

keyword arguments:- are sending arguments in a pair(a = 2)

def all_(*name):
    print(name)
all_('sneha','gunta','jagadeesh','paila','sindhu')

variable length argument:- Adding a (* call it as args) before a variable at parameters we can pass tuple of arguments and can be access with indexing
def all_(*name):
    print(name[3])
all_('sneha','gunta','jagadeesh','paila','sindhu')

keyword length arguments:-

def details(**data_):
    print(data_.keys())
details(name='sneha',age=21,location='vizag',batch=6)

return :- return keyword used inside the function,once the return is executed means it will get back to calling with return values
'''
def all_(a,b):
    return a-b
print (all_(7,8))

