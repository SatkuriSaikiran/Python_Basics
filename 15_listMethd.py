'''
# append()
fruit = ["apple","manago","banana"]
print(fruit)
fruit.append("grapes")
print(fruit)

# extend()
lang = ["Enlish","Telugu","Hindi"]
lang1 = ["French","Ger"]
lang.extend(lang1)
print(lang)

# index()
lang = ["English","Telugu","Hindi"]
print(lang.index("English"))
print(lang.index("English"),lang.index("Hindi"))

# insert()
lang = ["English","Telugu","Hindi"]
lang.insert(0,"German")
print(lang)
lang.insert(2,"French")
print(lang)

# count
list_int = [1,2,3,8,10,4,4]
print(list_int.count(4))

# remove()
lang = ["English","French","Telugu","Hindi"]
lang.remove("French")
print(lang)

# pop()
lang = ["English","French","Telugu","Hindi"]
lang.pop(1)
print(lang)

# reverse()
lang = ["English","French","Telugu","Hindi"]
lang.reverse()
print(lang)

# sort
list_int = [1,2,3,5,7,9,4]
list_int.sort()            # sort in assescending order
print(list_int)

list_int.sort(reverse=True) # sort in descending order
print(list_int)
'''