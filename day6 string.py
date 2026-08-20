DAY-6 Strings

Strings :- sequence of characters

string operations
1. Indexing:- is used to get char that you looking to acess
they are two types of indexing
1. positive 2. negative
1. if the positive number starts from zero.
2. if the negative number starts from -1
 ---> syntax:- print(variable_name[index_position])
    sneha
   [0,1,2,3,4] +ve

syntax--->  print(variable_name[negative index_position])
      sneha
 -5,-4,-3,-2,-1 -ve

text = 'python'6
print(text[3])
print(text[-2])

text= 'python is a programming language'
print(text[17])

2. length(len):- len() is built in function that is used get number of char present in the string
 syntax ----> len(variable_name)

text= 'python is a programming language'
print(len(text))

3. slicing:- is used to acess the particular part from the string.
  syntax ---> variable_name[start:end]

text= 'python is a programming language'
print(text[12:23])
print(text[10:])
print(text[:23])

text = 'madam'
print(text[::-1])

4. upper() :- used to convert all small character into capital
text= 'python is a programming language'
print(text.upper())

5. lower() :- used to convert all capital character into small
text= 'python is a programming language'
print(text.lower())

6. Index:- is called the index position of the character 
 Syntax ---> variable_name.index('substring',start,end)
jack = sneha
print(jack.index('e'))
print(jack[3])

text= 'python is a programming language'
print(text.index('i', 9))
print(text[7])

7.replace:- used to replace old substring with new substring
  syntax ---> variabl_name.replace(ol,new)

text= 'python is a programming language'
print(text.replace('a'),joyful))

8. Split():- is used to seperate the string based on the given substring
  Syntax :- variable_name.split(substring)
text= 'python is a programming language'
print(text.split(' '))

9. count() :- used to count number of occurances of an substring
  Syntax ---> variable_name.count('substring')

text = 'python is a programming language'
print(txt.count('a',1,12))
