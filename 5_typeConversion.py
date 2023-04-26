# ---------------Implicit type conversion---------------

'''python automatically convert one to another'''
a = 10   # int
b = 20.5 # float
c = b+a # float           # or a+b
print(c)
print(type(c))

# NOTE in this implicit type we are unable to add string and int/float soo we use Explicit type for it

# ---------------Explicit type conversion----------------

'''user convert data type'''

a = 100  #int
b = "40" #str
c = int(b)
d = a+c
print(d)