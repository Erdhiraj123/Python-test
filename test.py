# Prime number 1 to 71 using for loop
'''
for i in range(1,71):
    count=0
    for x in range(2,i//2+1):
        if i%x==0:
            count+=1
            
    if count==0:
        print(i) 
'''
#fibonacii series using for loop
'''
a=0
b=1
print(a,b,end= " ")
for i in range(10+1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c 
'''
#using while loop to continue the program
'''
while True:
    print("hello Dheeraj")
    ch=input("Do you want to continue")
    if ch!='y' and ch!='Y':
        break 
        
'''
# To check the prime number or not using while loop
'''
user=int(input("Enetr any Number:"))
count=0
loop=2
while loop<=user//2:
    if user%loop==0:
        count+=1
        break
    loop+=1

if count==0:
    print("prime Number")
else:
    print("Not Prime")

'''
#fibonacii series using while loop
'''
a=0
b=1
count=0
print(a,b,end=" ")
while count<=10:
    c=a+b
    a=b
    b=c

'''    
#Add even and odd number 1 to 100 using while loop
'''
odd=0
even=0
x=0
while x<=100:
    if x%2==0:
        even+=1
    else:
        odd+=1

print(even,odd)

'''
#Check if the user is valid or not 
'''
import random
user="dhiraj"
mob="9399790279"
password=1234
capcha=random.randint(1,100)
print(capcha)
u=input("User Name")
p=int(input("Password"))    
c=int(input("capcha"))
if (u==user or u==mob) and p==password and c==capcha:
    print("access Permited")

else:
    print("Access Denied")
'''

#prime number 1 to 100 using while loop
'''
user=0
while user<=100:
    count=0
    loop=2
    while loop<=user//2:
        if user%loop==0:
            count+=1
            break
        loop+=1
    if count==0:
        print(user)
    user+=1

'''
# To Check minimum values of the list
'''
a=[]
loop=int(input("How many value you want to put in A:"))
for i in range(loop):
    user=eval(input("Values:"))
    a.append(user)
print(min(a))

'''
#count how many data type in this programs
'''
a=[]
count=0
loop=int(input("How many value:"))
for i in range(loop):
    user=eval(input("Values:"))
    a.append(user)
for y in a:
    if (type(y)==int or (type(y)==float)):
        count+=1
print(a)
print(count)

'''

#addition of two list
'''
a=[]
b=[]
c=[]
loop=int(input("How many values in A:"))
for i in range(loop):
    user=eval(input("values"))
    a.append(user)
loop=int(input("How many values in B:"))
for i in range(loop):
    user=eval(input("Values"))
    b.append(user)
print(a)
print(b)
if (len(a)>(len(b))):
    for i in range(len(b)):
        c.append([a[i]+b[i]])
else:
    for i in range(len(a)):
        c.append([a[i]+b[i]])

print(c)

'''
#check how many data tpes in this list
'''
a=[]
complex1=0
string1=0
bool1=0
loop=int(input("how many values in a:"))
for i in range(loop):
    user=eval(input("Values"))
    a.append(user)
for y in a:
    if (type(y)==str):
        string1+=1
    elif(type(y)==bool):
        bool1+=1
    elif(type(y)==complex):
        complex1+=1
print(f'complex{complex1} string{string1}bool{bool1}')

'''