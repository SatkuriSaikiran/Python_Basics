# ----------------CREATE PARENT CLASS----------------
# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)
x = Person("sai","bunny")     
x.printname()   
# ------------------CREATE CHILD CLASS----------------
#

