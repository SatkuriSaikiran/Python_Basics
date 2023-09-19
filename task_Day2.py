'''
#1 Program to print the friends name follows with Hey dear nice to be your friend
a = input("Enter Name:")
print(a,"Hey dear nice to be your friend")

'''
'''
#2 Highest of two numbers
a = input("Enter the Number One")
b = input("Enter the Number Two")
if a<b:
    print(b,"is higher number")
else:
    print(a,"is higher number")
'''
'''
#3 Highest of three numbers
a = input("Enter the Number One")
b = input("Enter the Number Two")
c = input("Enter the Number Three")
if a<b and c<b:
    print(b,"is higher")
elif a<c and b<c:
    print(c,"is higher")
else:
    print(a,"is higher")


#4 Highest of Four numbers
a = input("Enter the Number One")
b = input("Enter the Number Two")
c = input("Enter the Number Three")
d = input("Enter the Number Four")
if a<b and c<b and d<b:
    print(b,"is higher")
elif a<c and b<c and d<c:
    print(c,"is higher")
elif b<a and c<a and d<a:
    print(a,"is higher")    
else:
    print(d,"is higher")

'''
'''
#6 to find the given number is even or odd
a = int(input("enter the number"))
if a%2==0:
    print(a,"is even number")
else:
    print(a,"is odd number")

'''
'''
#7 Check eligiblity of vote

a = int(input("Enter the age"))
if a>18:
    print("Eligible for VOTE")
else:
    print("Not eligible for VOTE")    
'''
'''
#8 to create a unique record of friend

# Ramu likes
Ramu = {"apple","blue","chess","cycling","swimming"}
# Laxman likes
Laxman = {"banaba","blue","ball","swimming","carrot"}
print(Ramu&Laxman)       # similar likes of both
print(Ramu|Laxman)       # Uniques
'''
'''
#9 ask 5 favorite fruits of your frd,store and display in a container
a = input("Enter the favorite fruit no1: ")
b = input("Enter the favorite fruit no2: ")
c  = input("Enter the favorite fruit no3: ")
d = input("Enter the favorite fruit no4: ")
A = [a,b,c,d]
print("the favorite fruits are: ",A)


#10 to find the square of given number
a = int(input("Enter a number: "))
b = a**2
print("The square of the",a,"is",b)


#11 Ask marks and give the results
a = int(input("Enter the Subject1 marks: "))
b = int(input("Enter the Subject2 marks: "))
c = int(input("Enter the Subject3 marks: "))
if a>=33 and b>=33 and c>=33:
    print("PASS")
else:
    print("FAIL")
Percentage = ((a+b+c)/300)*100
if Percentage>=80:
    print("Exellent")
elif Percentage<80 and Percentage==70:
    print("Very Good")
elif Percentage>=60:
    print("GOOD")
elif Percentage>=50:
    print("Average")
elif Percentage>=40:
    print("NOT BAD")
else:
    print("Better Luck Next Time")

'''
#12 Table
a =15
for i in range(1,11):
    print(a,"X",i,"=",a*i)

# To write the maths table

for x in range(11):
    print(10,"*",x,"=",x*10)




