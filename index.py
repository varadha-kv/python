'''a="varadha"
print(a)
b=58
print(b)
c=68.3
print(c)
d=[1,2,3,4,5] # list
print(d[0]) # print 1st index
print(d[-1]) # print last index
d.append(6) # add an element
print(d)
d.insert(2,9)
print(d)
d.pop()
print(d)
e=("varadha",19,"girl")
print(e)
f=list(e)
print(f)
f.append("student")
g=tuple(f)
print(g)'''

# user input

var = int(input("enter your age"))
print(type(var))

# check the number is positive or negative

w = int(input("enter a number"))
if(w>0):
    print("Positive")
else:
    print("Negative")

# check the number is even or odd

h = int(input("enter a number"))
if(h%2==0):
    print("even")
else:
    print("odd") 

# check if a person is eligible for vote

age = int(input("enter your age"))
if(age>=18):
    print("you are eligible for vote")
else:
    print("you are note eligible for vote")

# check whether a number divisible in 5

num = int(input("enter a number"))
if(num/5==0):
    print("it is divisible in 5")
else:
    print("it is not divisible in 5")   

# check if a character is a vowel or consonant

char = input("enter a character")
if(char in "aeiouAEIOU"):
    print("vowels")
else:
    print("consonent")

# check whether a number is zero positive or negative

c = int(input("enter a number"))
if(c==0):
    print("zero")
elif(c>0):
    print("positive")
else:
    print("negative")

# check whether a number is multiple of 3 and 7

q = int(input("enter a number"))
if(q % 3 == 0 and q % 7 == 0):
    print(q,"is a multiple of 3 and 7")
else:
    print(q,"is not a multiple of both")

# take a password and check it is matches to predefined password

word = input("enter your password")
if(word=='vara123'):
    print("matches")
else:
    print("mismatch")

# check whether a year is leap year or not

year = int(input("enter a year"))
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("it is leap year")
else:
    print("it is not leap year")

# Simple calculator using if-elif (add, subtract, multiply, divide).

v = float(input("enter a number"))
r = float(input("enter a number"))
operator = input("enter a operator(+,-,*,/):")
if(operator== '+'):
    print("result:",{v+r})
elif(operator == '-'):
    print("result:",{v-r})
elif(operator =='*'):
    print("result:",{v*r})
else:
    print("result:",{v/r})

# check a number is divisible by 2 and 5

j = int(input("enter a number"))
if(j%2==0 and j%5==0):
    print("it is divisible by both")
else:
    print("it is not divisible by both")

# check whether a number lies in b/w 1 and 100

s = float(input("enter a number"))
if(1<=s<=100):
    print("it in b/w 1 and 100")
else:
    print("it is not in b/w 1 and 100")

# find the smallest b/w three numbers

num1 = int(input("enter a num"))
num2 = int(input("enter a num"))
num3 = int(input("enter a num"))
if(num1<num2 and num1<num3):
    print(num1,"is a smallest number")
elif(num2<num1 and num2<num3):
    print(num2,"is a smallest number")
else:
    print(num3,"is smallest number")

# ATM withdrawal (check balance before withdrawal).

balance = 5000
amount = int(input("enter the amount"))
if(amount>balance):
    print("insufficient bank balance")
elif(amount<0):
    print("amount should be positive")
else:
    new = balance-amount
    print(new)

# Movie ticket pricing: Child (<12) → ₹100 Adult → ₹200 Senior (>60) → ₹150

child = 100
adult = 200
sinior = 150
ticket = int(input("enter age"))
if(ticket<12):
    print(child)
elif(12<=ticket<=60):
    print(adult)
else:
    print(sinior)

#loop - for

# print number from 1 to 10

for i in range(1,11):
    print(i)

#  print even number from 1 to 20

i = 2
for i in range(2,21,2):
    print(i)

# print odd number from 1 to 20

i = 1
for i in range(1,21,2):
    print(i)

 print multiplication table of a table

mul = int(input("input a number"))
for i in range(1,11):
    print(mul*i) 

# print 1 to 10 in reverse

for i in range(10,0,-1):
    print(i)

print the sum of numbers 1 to n

n = int(input("enter n"))
total = 0
for i in range(1,n+1):
    total+=i
    print(total)

# print the square of 1 to 10

for i in range(1,11):
    print(i**2)