'''
# string reverse

words = 'madam'
empty_str = ''
for i in words:
    empty_str = i + empty_str
    print(empty_str)
if empty_str == words:
    print(f'{words} is a palindrome')
else:
    print(f'{words} is not a palindrome')
.............

# Amstrong number

num = int(input('enter a number: '))
length = len(str(num))
amstrong = 0
for i in str(num):
    amstrong = amstrong + int(i)**length
    print(amstrong)
if amstrong == num:
    print(f'{num} is amstrong number')
else:
    print(f'{num} is not a amstrong number')
............

# perfect number
1+2+3=6
1+2+4+7+14=28

num = 28
sum = 0
for i in range(1,num):
    if num % i == 0:
        sum += i
        print(sum)
if sum == num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')
.......
# fibnocies series

num = 0
num_2 = 1
print(num,num_2,end = ' ')
for i in range(1,10):
    num_3 = num + num_2
    num = num_2
    num_2 = num_3
    print(num_3,end=' ')
...........  



