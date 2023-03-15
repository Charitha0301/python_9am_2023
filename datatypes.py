# a=2
# print(a)
# print(type(a))
# name='''Charitha sree is learning 'Python' in Digital Lync'''
# print(name)
# print(type(name))
# print(name[:-1])
# print(name[-7:100])
# print(name[-1:-50])
# print(name[2:-2])
# s="ABCDEFGHIJKL"
# print(s[7:2:-2])
# print(s[-1:2:-2])
# print(s[0:-1])
# print(s[-1:10])
# print(len(s))
# print(s[0:].lower())
# print(s[0].lower()+s[1:8]+s[:12].lower())
# x="Python is a programing language"
# print('python' in (x))
# print('A' in (x))
# print('programing' in (x))
# print('python' in (x))

# a=12
# b=0
# b=a
# print(float(a))
# print(str(a))
# print(bool(a))
# a=b
# print(bool(b))

# l=[10,20,30,40,50] #lists
# print(l)
# l.append(10)
# l.append(60)
# l.append(80)
# l.append(100)
# print(l)
# l.remove(10)
# print(l)

# t=(10,20,30,40)#tuple
# print(t)

# set={1,2,3,'charitha',4,5}
# print(set)
# # print(set[1])
# s.add(30)
# s.remove(7)
# print(set)


# r=range(1,10)
# print(r[7])
# print(r[-1])
# r1=r[1:5]
# if x in r1:
#     print(x)

# r=int(input('enter any number:')) #range
# r=range(10,50)
# # r=range(1,50,2)
# r=range(50,1,-2)
# for x in r:
#     print(x)

# name=('charitha'+'sree')  #arthematical operators
# name=('charitha'+'10')
# name=('charitha'+10) #typeErroR
# print(name)
# print(type(name))
# x=(3*'charitha')
# x=('charitha'*'sree') #typeErroR
# # print(x)

# print(10/2)
# print(10//2)
# print(10.5//2)
# print(10%2)
# print(10**2)
# print(2**10)
# print('charitha'*False) #empty output is empty
# print('charitha'*True)
# print('charitha'*int(3))

# r='charitha'  #relative operators
# r1='sree'
# print(r<r1)
# print(r<=r1)
# print(r>r1)
# print(10<20<30>40)

# print(10==20==30)  #equality operators
# print(20==20==20)
# print(10 != 20)
# l1=[10,20,30,40]
# l2=[10,20,30,40]
# print(id(l1))
# print(id(l2))
# print(l1 == l2)
# print(l1 is l2)
# print(l1 != l2)

#Create a username and password input  #Logical operators
# username=input('Enter your username:').lower()
# pwd=input('Enter your password:')
# if username =='charitha sree' and pwd =='Madunala':
#     print('Valid user')
# else:
#     print('Invalid user')    

# x=int(input('Enter a number:'))
# if x == (1,10) or (10,21):
#     print('Belongs to x range')
# else:
#     print('Not type of row') 

# y=int(input('Enter any number:'))
# if y == 10 or 50:
#     print('Belongs to y')  
# else:
#     print('Does not belongs to y')

# print('charitha' or 'sree')
# print('charitha' or 'madunala')
# print('sree' or 'charitha')
# print(10 or 'sree')
# print([] or 'sree')
# print('' or 'sree')

# print(4^5)
# print(4&5)
# print(4*5)
# print(~5)

# a=10
# b=20
# c=50 if a>b else 60 
# print(c)

# a=int(input('Enter first number:'))  #nesting
# b=int(input('Enter second number:'))
# c=int(input('Enter third number:'))
# min=a if a<b and a<c else b if b<c else c
# print('The minimum value', min)

# s='charitha sree'  #membership operator
# print('cha' in s)
# print('cha' not in s)

# print(10+30/4*100) #operator precedence

#Read two int values from the keyboard and point the sum
# x=int(input('Enter first number:')) 
# y=int(input('Enter second number:'))
# print('The sum:', x+y)

#WAP to read the emplyee data from the keyboard and point that data
# eno=int(input('Enter emplyee no:'))   #input()
# ename=input('Enter employee name:')
# esalary=float(input('Enter emplyee salary:'))
# eaddress=input('Enter emplyee address:')
# married=eval(input('Is emplyee married? [True/False]'))
# print('Please confirm the below information')
# print('Enter emplyee no:',eno)
# print('Enter employee name:', ename)
# print('Enter employee salary:', esalary)
# print('Enter employee address:', eaddress)
# print('Is employee married?', married)

#WAP to read multiple values from the keyboard in a single line:
# a,b,c=(int(x) for x, in input ('Enter three values:').split())
# print('The sum:',a+b+c)

# a,b,c=(float(x) for x, in input ('Enter three values:').split())
# print('The sum:',a+b+c) 

# a,b,c,d,e,f=10,20,30,40,50,60
# print(a,b,c,d,e,f, sep='^') #separate attribute
# print(a,b,c,d,e,f, sep=';')
# print(a,b,c,d,e,f, sep='+')

# print('Hello!', end=' ') #end attribute
# print('Charitha', end=' ')
# print('sree', end=', ')
# print('Welcome to the India.')

# print(10,30,20,40, sep='+', end='')  #sep and end attributes
# print(50,60, sep='-')
# print(1,2,3,4,5, sep='*', end='')
# print(10,9,8,7, sep='%')

# print(10+30+20+4050-60) #arthematic operatos
# print(1*2*3*4*510%9%8%7)

# x='Charitha'
# y='Hyderabad'  #Replacement operator:{}
# z=21
# print('Hi! Iam {}, I live in  {} and Iam {} years old.'.format(x,y,z))
# print('Hi! Iam {0}, I live in  {1} and Iam {2} years old.'.format(x,y,z))
# print('Hi! Iam {a}, I live in  {b} and Iam {c} years old.'.format(a=x, b=y, c=z))

# a=10
# print('a value: %i' %a)  #print() with formatted string
# print('a value: %f' %a)
# print('a value: %s' %a)
# print('a value: %d' %a)

# a=10
# b=20
# c=40
# print('a=%d, b=%i, c=%f' %(a,b,c))

# a='charitha'
# b=[10,20,30,40]
# c=30
# print('Hello %s roll number: %i your list of marks: %s' %(a,c,b) )

# name='Charitha'
# name1='Shiva'
# name2='Sameena'
# marks=[90,80,70,60]
# marks1=[50,40,30,20]
# marks2=[10,20,30,40]
# rolno=3
# rolno1=2
# rolno2=1
# print('Hello %s roll number %i, your marks list is:%s' %(name,rolno,marks))
# print('Hello %s roll number %i, your marks list is:%s' %(name1,rolno1,marks1))
# print('Hello %s roll number %i, your marks list is:%s' %(name2,rolno2,marks2))











