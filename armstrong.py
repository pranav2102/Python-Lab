#Name: Pranav Badgujar
#Div- P
'''Write a python program to find user entered no. is an armstrong no. or not'''

x=int(input('Enter a three digit number'))
x1=x//100
r1=x%100
x2=r1//10
r2=r1%10


z=(x1)**3+(x2)**3+(r2)**3
if x==z:
   print('Given no is armstrong no')

else:
   print('Given no is not a armstrong no')

