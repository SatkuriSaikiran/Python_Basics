'''
my_set = {1,2,3,9,6,7}
print(my_set)

my_set = {1,2,3,9,6,7,"hello world",4,10}
print(my_set)

a = {"a","b","c"}
print(a[0])      # not support for indexing

my_set = {1,2,3,9,6,7}
my_set.add(3)           # to add single item
print(my_set)
my_set.update([10,11,12]) # to add multiple items
print(my_set)

my_set = {1,2,3,9,6,7}
my_set.remove(2)
print(my_set)

# set operation
# union - set of all elements in both
a = {0,1,2,5}
b = {3,4,5,5,3}
print(a|b)
'''

# intersection - elements that are common
a = {0,1,4,2,5}
b = {3,4,5,5,3}
print(a&b)