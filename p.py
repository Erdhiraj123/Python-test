#Print first 10 natural number using for and while loop in python

# using while loop
i=1
while i<=10:
    print(i)
    i=i+1
    
#using for loop
for i in range(1,11):
    print(i)
    
#calculates number of days between two dates

from datetime import date
firstdate=date(2023,1,3)
seconddate=date(2023,2,1)
finaldate=(seconddate-firstdate)
print(finaldate.days)

#write a program to find average number of list in given list

a=[]
list=int(input("How many value in A:"))
for i in range(list):
    user=int(input("Values:"))
    a.append(user)
print(a)
add=sum(a)
print("sum of list:",add)
average=add/list
print("average number of list:",average)

# Find sum of digits of given number 

a=int(input("Please Enter values:"))
sum=0
while a>0:
    sum=sum+a%10
    a=a//10
print("sum of digits number is:",sum)

#check leap year using python

year=int(input("Enter year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        print("Leap year")
    print("Leap year")
else:
    print("Not Leap year")
    
#Python program to reverse a string using for loop

a=input("Enter any charecter:")
for i in range((len(a)-1),-1,-1):
    print(a[i],end=" ")
    
#Reverse a string using indexing

a=input("Enter any Charecter:")
print(a[::-1],end=" ")


#Python Program to check if two string are anagram or not

str1="night"
str2="thing"
if (sorted(str1)==sorted(str2)):
    print("Anagram string")
else:
    print("Not anagarm")

#Python program to find the area of circle

a=float(input("Enter first values:"))
b=float(input("Enter second values:"))
c=float(input("Enter third values:"))
s=a+b+c/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of circle is:",area)


#Python iterate list with index

list1=[1,2,3,4,3,12,11]
l1=len(list1)
for i in range(l1):
    print((i,list1[i]),end=" ")
   

#Python add list to list

l1=[1,2,3,3,1,2,3]
l2=[]
loop=int(input("How many value in l2:"))
for i in range(loop):
    user=eval(input("value"))
    l2.append(user)
    
l1.append(l2)
print(l1)


#python Random choice from list
import random
l2=[]
loop=int(input("How many value in l2:"))
for i in range(loop):
    user=eval(input("value"))
    l2.append(user)
    
print("Random choice is:",random.choices(l2,k=3))


#Python dict inside list

dict1={"Name":"Dheeraj Yadav","Location":"Noida"}
list=[True,"Yadav",1,3,1]
convert=dict1.copy()
list.append(convert)
print(list)
