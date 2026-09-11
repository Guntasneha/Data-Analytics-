'''
print("hello good morning")

# perform operation as below
a = 25
b = 15
print(a + b)
'''
# tokens---> keywords, variables, operators, punctuators [], (), {}
#variables ----> should not start with number, space, symbols, and also no space
#between words
batch = ['PFS-6','DA-6']
print(batch)
print(type(batch)) # everything is an object (pop ---> oop)
# len() ---> returns the number of items in a collection

print(len(batch))

# idle is colorcoding editor (violet ---> built-in functions)
# add 3 mor students names into it
# list ---> collection ---> append(), extend(), insert()

batch.append('saketh')
#print(batch)
batch.extend(['akash','anil'])
#print(len(batch))
#print(batch)
batch.insert(0,'sai')#inserts given value at specific index
#print(batch)
batch.insert(-1,'python') # value before index
print(batch)
print(len(batch))

# indexing---> [] ---> index starts at 0 and ends at len(obj)-1
# and also in reverse manner it is -1 to len(obj)
#print(batch[0])
#print(batch[4])
#print(batch[32]) indexerror--> length is only 7 we are accesing extra

# slicing---> group of values [start:end] # start is included,end is excluded
#print(batch[0:3])
#print(batch[4:6])
#print(batch[6:7])

# last 3 elements --> we prefer negative index values
#print(batch[-3:])
# first 3 elements
#print(batch[:3])
print(batch)
# striding ---> [start:end:step]
print(batch[::2]) # it skips 1 element from start
print(batch[::3]) # it skips 1 element from start
print(batch[1:5:2]) # first perform batch[1:5] --> then skip 1 element

# tryout ---> such kind
print(batch[:7:4])
print(batch[7::4])
print(batch[1::5])
print(batch[1:7:-2])
print(batch[-1:-4:-1])

