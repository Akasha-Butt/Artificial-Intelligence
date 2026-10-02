######################## TASK 1 ########################

# x=1
# if x>0:
#     print("these are two comments");


######################## TASK 2 ########################

# print("Statement 1")
# print("Statement 2")

# We can print our statements in different ways

# print("Statement 1") ; print("Statement 2");


######################## TASK 3 ########################

# x=1
# if x>0:
# print("this statement has no indentation");
# print("This statement has no indentation");


######################## TASK 4 ########################

# x=1
# if x>0:
#     print("this statement has indentation");
#     print("This statement has indentation");


######################## TASK 5 ########################

# x=1
# if x>0:
#     print("this statement has single space+indentation");
#     print("This statement has single space+indentation");


######################## TASK 6 ########################

# a=123
# print(type(a))
# b=(-4587)
# print(type(b))
# c=0
# print(type(c))
# g=1.03
# print(type(g))
# h=-11.23
# print(type(h))
# i=.34
# print(type(i))
# j=2.12e-10
# print(type(j))
# k=5E220
# print(type(k))


######################## TASK 7 ########################

# x=complex(1,2)
# print(type(x))
# print(x)
# (1+2j)

# z=1+2j
# print(type(z))

# z=1+2J
# print(type(z))


######################## TASK 8 ########################

# x=True
# print(type(x))
# y=False
# print(type(y))


######################## TASK 9 ########################

# str1="string with double quotes"  
# print(str1)

# str2='string with single quotes'
# print(str2)

# str3="string start with double and end with single quotes'
# print(str3)

# str4='string start with single and end with double quotes"
# print(str4)

# str5="Day's" # single quote within double quotes
# print(str5)

# str6='Day"s' # double quote within single quotes
# print(str6)


######################## TASK 10 ########################

# print("This is a backslash (\\) mark.")
# print("This is a tab \t key.")
# print("These are \'single quotes\'")
# print("These are \"double quotes\"")
# print("This is a new line\nNew line.")


######################## TASK 11 ########################

# string1="PYTHON TUOTORIAL"
# print(string1[0])
# print(string1[-15])
# print(string1[14])
# print(string1[-1])
# print(string1[4])
# print(string1[-11])
# print(string1[16]) # gives error because index 16 does not exist


######################## TASK 12 ########################

# my_list1=[5,12,13,14] # list containing integer values
# print(my_list1)

# my_list2=['red','blue','black','white'] # list containing string values
# print(my_list2)

# my_list3=['red',12,112.12] # list containing different data types
# print(my_list3)


######################## TASK 13 ########################

# my_list=[]
# print(my_list)


######################## TASK 14 ########################

# color_list=["Red","Blue","Green","Black"] 
# The list contains 4 elements. Indices start at 0 and end at 3.

# print(color_list[0]) # returns the 1st element
# print(color_list[1],color_list[3])
# print(color_list[-1])
# print(color_list[4]) # gives error because this index does not exist


######################## TASK 15 ########################

color_list1=["Red","Blue","Green","Black"]

print(color_list1[0:2]) # selects the first two items
print(color_list1[1:2]) # selects the second item
print(color_list1[1:-2]) # selects items using negative index
print(color_list1[:3]) # selects the first three items
print(color_list1[:]) # creates a copy of the original list