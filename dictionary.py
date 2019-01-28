#Name : Pranav Badgujar
#Div - P


x = int(input('No of Students : '))
d = {}
for i in range(x):
 print('students no' ,i+1)
 n=input('Name : ')
 g=int(input('Gr no :'))
 b=input('Branch: ')
 d[g] = (n,b)
print(d)

