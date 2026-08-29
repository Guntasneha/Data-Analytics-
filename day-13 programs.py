'''
# even or odd

ran_ = int(input('enter a number: '))
for j in range(1,ran_+1):
    if j % 2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')
# print only even numbers

ran_ = int(input('enter a number: '))
for j in range(1,ran_+1):
    if j % 2 == 0:
        print(f'{j} is even')
    
# print only odd numbers

ran_ = int(input('enter a number: '))
for j in range(1,ran_+1):
    if j % 2 != 0:
        print(f'{j} is odd')

# if the list is given then the  print even or odd 

nums = [23,78,97,5]
for j in nums:
    if j % 2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')

# finding the number of vowels count are present

words_ = input('enter a word: ').lower()
vowels = 'aeiou'
count = 0
for i in words_:
    if i in vowels:
        count += 1
        print(f'{i} in vowel')
print(count)

# finding the number of vowels count are present

words_ = input('enter a word: ').lower()
vowels = 'aeiou'
count = 0
for i in words_:
    if i not in vowels:
        count += 1
        print(f'{i} in consonants')
print(count)

# finding the number of consonants count are present

words_ = input('enter a word: ').lower()
vowels = 'aeiou '
count = 0
for i in words_:
    if i not in vowels:
        count += 1
        print(f'{i} in consonants')
print(count)

# remove dupliacte numbers from the list

digits = [1,2,3,1,5,3]
empty_ = []
for i in digits:
    if i not in empty_:
        empty_.append(i)
print(empty_)

# duplicate from the tuple

digits = (1,2,3,5,1,3)
empyt = ()
for x in digits:
    if x in digits:
        empty += 
        print(f'{x} is a duplicate ')
print(empty)

# spaces remove and how many count in an word

words = 'python is an programming language'
txt = words.split(' ')
print(txt)
print(len(txt))

'''






