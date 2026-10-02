######################## TASK 1 ########################

# count=0
# while(count<3):
#     count=count+1
#     print("Hello Greek")


######################## TASK 2 ########################

# count=0
# while count<3:count+=1 ; print("Hello Greek by While loop in single line ")


######################## TASK 3 ########################

# list=["geeks","for","geeks"]
# for i in list:
#     # list[1]="Akasha"  mutable
#     print(i)


######################## TASK 4 ########################

# tuple=("Apple","Banana","Grapes")
# for tup in tuple:
#     # tuple[1]="Akasha"   immutable
#     print(tup)


######################## TASK 5 ########################

# arr={1,2,3,4,5,6,7,8}
# for a in arr:
#     print(a)


######################## TASK 6 ########################

# list=['hello','world',1,'done']
# for l in range(len(list)):
#     print(list[l])


######################## TASK 7 ########################

# str='geeksforgeeks'
# for L in str:
#     if L=='e' or L=='s':
#         continue
#     print('current letter',L)


######################## TASK 8 ########################

# str='geeksforgeeks'
# for L in str:
#     if L=='f' or L=='o':
#         break
#     print('current letter',L)


######################## TASK 9 ########################

# def my_function():
#     print("Hello World")
#
# my_function()


######################## TASK 10 ########################

# def addition(a,b):
#     print(a+b," is product")
#
# addition(3.4,5)


######################## TASK 11 ########################

# def country(country1='Norway'):
#     print("I am from ",country1)
#
# country('Pakistan')
# country('Turkey')
# country()


######################## TASK 12 ########################

# list=['hello','world','done',22,'Python']
#
# def List(a):
#     for i in a:
#         print(i)
#
# List(list)


######################## TASK 13 ########################

# def Return(y):
#     return y+7
#
# print(Return(45))
# print(Return(7))


######################## TASK 14 ########################

# def KeyWords(ch1,ch2,ch3):
#     print('The Youngest child is '+ ch3)
#
# KeyWords(ch3='Harry',ch1='Peter',ch2='john')


######################## TASK 15 ########################

# class my_Class():
#     x=60
#     name='Akasha'
#     dept='BSIT'
#     roll_nmbr=31
#
# o1=my_Class
# print(o1)
# print(o1.x)
# print(o1.name)
# print(o1.dept)
# print(o1.roll_nmbr)


######################## TASK 16 ########################

# class Student:
#     uni_name='PUGC'
#     city='Gujranwala'
#
#     def __init__(self,name,dept,rollnmbr):
#         self.name=name
#         self.dept=dept
#         self.rollnmbr=rollnmbr
#
# s1=Student('Akasha','BSIT',31)
# s2=Student('harry','BSIT',32)
# s3=Student('Peter','BSIT',33)
# s4=Student('Lucy','BSIT',34)
# s5=Student('John','BSIT',35)
# s6=Student('Logans','BSIT',36)
#
# print(s1.name,s1.dept,s1.rollnmbr)
# print(s2.name,s2.dept,s2.rollnmbr)
# print(s3.name,s3.dept,s3.rollnmbr)
# print(s4.name,s4.dept,s4.rollnmbr)
# print(s5.name,s5.dept,s5.rollnmbr)
# print(s6.name,s6.dept,s6.rollnmbr)


######################## TASK 17 ########################

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def hello(self):
#         print('My name is '+ self.name)
#
# p1=Person('Akasha',20)
# p1.hello()