'''
list comprehension:- is the shortest form of the syntax to create a new list.
 Syntax1 ---> [expression loop condition]
 Syntax2 ---> [expression loop condition else loop]
 
old_ = [1,2,5,8]
new_ = [i for i in old_]
print(new_)

old_ = 'python'
new_ = [i for i in old_]
print(new_)

old_ = [1,2,3,4,5]
new_ = [i for i in old_ if i%2==0]
print(new_)

nested comprehension or (matrix):- using list comprehension generating list inside list.

any_ = [[i*j for i in range(1,4)] for j in range(1,10)]
print(any_)

sum = [[1,2,3],
     [4,5,6],
     [7,8,9]]

data_ = [num for i in sum for num in i]
print(data_)

.................

Generator functions:- is a special function which generates one value at a time.

def all_():
    for j in range(1,10):
        yield j
j = all_()
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))
'''
