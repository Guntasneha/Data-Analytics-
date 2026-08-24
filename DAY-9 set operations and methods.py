DAY-9 set operations and methods

Set:- is unordered collection of elements
No duplicate allowed in the set
set is represented by {}.
nums = {1,2,3,2}
print(nums)

....

Operations:-
 
1. Union() :- the union() will combine two set into a single set.
 Syntax ---> set_1.union(set_2) or set_1 | set_2
data_ = {1,2,3,4}
nums = {5,6}
print(data_.union(nums))  #this is for syntax method
print(data_ | nums)  # if we can write in simple pipe method

2. Intersection() :- it will gives us the common elements from both sets
 syntax ----> set_1.intersection(set_2) or set_1 & set_2
data_ = {1,2,3,4}
nums = {4,5,6}
print(data_.intersection(nums))
print(data_ & nums)

3. difference() :- it will display the different elements from set_1, but not the set_2 elements
 syntax ----> set_1.difference(set_2) or set_1 - set_2
data_ = {1,2,3,4}
nums = {4,5,6}
print(nums - data_)
print(nums.difference(data_)) # {5,6}
print(data_ - nums)
print(data_.difference(nums)) # {1,2,3}

4. symmetric_difference() :- difference elements from both
 syntax ----> set_1.symmetric_difference(set_2) or set_1 ^ set_2 
data_ = {1,2,3,4}
nums = {3,4,5,6}
print(data_.symmetric_difference(nums))
print(nums ^ data_)

.....

Methods:-

1. add() :- this method will add only one element at a time
 syntax ----> set.add(elements)
data_ = {1,2,3,4}
print(data_)
data_.add(7)
print(data_)

2. update() :- we can add more one elements by using update method.
 Syntax ---> set.update([elements]) or set_1.update(set_2)
data_ = {1,2,3,4}
nums = {4,5,6}
print(data_)
data_.update([8,9])
print(data_)
data_.update(nums)
print(data_)

3.remove() :- this method will delete the given element from the set, if the element is not present in the set, it will raise error
data_ = {1,2,3,4}
data_.remove(3)
print(data_)
data_.remove(5) # if the set 5  in not in set because it will the error 

4. discard () :- this method is used to delete the elements from the set,but never raise any error even the element not inside set.
  Syntax ----> set.discard(element)
data_ = {1,2,3,4}
data_.discard(7)
print(data_)
data_.discard(1)
print(data_)

5. clear() :- this method is used to delate all elements from the set and it will written empty set
  Syntax ---> set.clear()
data_ = {1,2,3,4}
print(data_)
data_.clear()
print(data_)






