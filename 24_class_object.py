'''
# create a class and object
class Myclass:                   # here Myclass is the class
    x=5                          #p1 is the object
p1 = Myclass()
print(p1.x)


# use the _init_() function to assign values to object properties, or other operations that are neccessary to do when the object is being created

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1 = Person("John",20)
print(p1.age)
print(p1.name)

 
# The __str__() function controls what should be returned when the class object is represented as a string. 
# If the __str__() function is not set, the string representation of the object is returned:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


## OBJECT METHODS
# insert a function that prints a greeting, and execute it on the p1 object
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is "+self.name)
p1=Person("John",20)
p1.myfunc()

'''
 
        