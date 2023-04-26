a = 10                # int
b = 20.5              # float
c = 2+5j              # complex
print(type(c))
                      # list
d = [10,20,30]
print(d[1])
print(d[0])

fruit = ["apple","mango","banana"]
print(fruit[2])
print(type(fruit))
                    #insert an item in the list
fruit.insert(0,"grapes")
print(fruit)
                               # tuple
months = ("jan","feb","mar")
print(months)
# months.insert(0,"hello")        # NOTE in tuple tuple we can not insert any thing     
print(type(months))
                               # string
e = "sai"
print(type(e))                            
a = '''saikiran
age = 20
place = rampoor'''
print(a)
print(type(a))                    
                              #set (not a data type)
f = {1,2,3,9,5,8,7,5,5}
print(type(f))
print(f)
                              #dictionary
d = {1:"bunny",2:"kiran",6:"sai"}
print(d)
print(type(d))
print(d[2])