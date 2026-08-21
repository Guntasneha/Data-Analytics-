DAY 7 LIST

List:- collection of different datatypes that separated by ,(comma) and it is represented by []

1. Indexing:-

positive index :- 0
negative index :- -1

s0 = [1,2,3,4,'python']
print(so[4][2])
print(so[-1])
all_ = [12,[1,'python',[1,4],(78,[6,7])],['java',78]]
print(all_)

2. data

data_ = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]
print(data_)
print(data_[1][2][1][2])

3. len():- the function is used to find the number of items present inside list
 Syntax ---> len(variable_name)

data_ = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]
print(len(data_))
print(len(data_[1][2]))

4. slicing:-

data_ = [1,2,3,4,5,6,7]
print(data_[2:6])

5. concandination:- 

a = [1,2]
b = [3,4]
print(a+b)

....

methods

1. Append() :- will add the new items into list at last index position.
   Syntax ---> variable_name.append(item)

go = [1,2]
print(go)
go.append(3)
print(go)
go.append(4)
print(go)

2. extend() :- extend will add the items into a list at last index position, but it will give each value as one index inside the list. 
   Syntax ----> variable_name.extend(items)

go = [1,2]
go.extend('python')
print(go)

3. po() :- it is used to remove item for the list and it will delete based on the index position
   Syntax ---> variable_name.pop(index_position)

m = [1,2,3,4]
m.pop(3)
print(m)

4. remove :- will delete items based on the value given in it.
    Syntax ---> variable_name.remove(value)

m = [5,1,2,3,4,'python']
m.remove('python')
print(m)






