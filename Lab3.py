##################TASK 01####################
#  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

#for number in range (1500,2700) :
# if number%7==0 and number%5==0 :
#   print (number)

##################TASK 02####################
# Write a Python program to convert temperatures to and from Celsius, Fahrenheit.

c = input("Enter temperature in Celsius: ")
f = (c * 9 / 5) + 32

print(c, "C is", f, "in Fahrenheit")

f = input("Enter temperature in Fahrenheit: ")
c = (f - 32) * 5 / 9

print(f, "F is", c, "in Celsius")


##################TASK 03####################
# Write a Python program to guess a number between 1 to 9.
#
# number = 7
#
# while True:
#     guess = int(input("Guess a number between 1 and 9: "))
#
#     if guess == number:
#         print("Well guessed!")
#         break


##################TASK 04####################
# Write a Python program to construct the following pattern.
#
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()
#
# for i in range(4, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()


##################TASK 05####################
# Write a Python program to reverse a word.
#
# word = input("Enter a word: ")
#
# reverse = word[::-1]
#
# print("Reversed word:", reverse)


##################TASK 06####################
# Write a Python program to count the number of even and odd numbers from a series of numbers.
#
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# even = 0
# odd = 0
#
# for number in numbers:
#     if number % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# print("Number of even numbers:", even)
# print("Number of odd numbers:", odd)


##################TASK 07####################
# Write a Python program to print each item and its type from a list.
#
# datalist = [1452, 11.23, 1+2j, True, 'w3resource',
#             (0, -1), [5, 12], {"class": "V", "section": "A"}]
#
# for item in datalist:
#     print(item, type(item))


##################TASK 08####################
# Write a Python program to print all numbers from 0 to 6 except 3 and 6.
# Use the 'continue' statement.
#
# for number in range(7):
#     if number == 3 or number == 6:
#         continue
#
#     print(number)


##################TASK 09####################
# Write a Python program to get the Fibonacci series between 0 to 50.
#
# a = 0
# b = 1
#
# while a <= 50:
#     print(a, end=" ")
#     a, b = b, a + b


##################TASK 10####################
# Write a Python program to create a two-dimensional array.
# The elements of the array are i*j.
#
# m = int(input("Enter number of rows: "))
# n = int(input("Enter number of columns: "))
#
# array = []
#
# for i in range(m):
#     row = []
#
#     for j in range(n):
#         row.append(i * j)
#
#     array.append(row)
#
# print(array)


##################TASK 11####################
# Write a Python program that accepts a sequence of lines as input
# and prints the lines in lowercase.
# Blank line terminates the input.
#
# while True:
#     line = input()
#
#     if line == "":
#         break
#
#     print(line.lower())


##################TASK 12####################
# Write a Python program that accepts a sequence of comma-separated
# binary numbers and checks which numbers are divisible by 5.
#
# numbers = input("Enter binary numbers separated by commas: ").split(",")
#
# result = []
#
# for number in numbers:
#     decimal = int(number, 2)
#
#     if decimal % 5 == 0:
#         result.append(number)
#
# print(",".join(result))


##################TASK 13####################
# Write a Python program that accepts a string and calculates
# the number of letters and digits.
#
# text = input("Enter a string: ")
#
# letters = 0
# digits = 0
#
# for character in text:
#     if character.isalpha():
#         letters += 1
#     elif character.isdigit():
#         digits += 1
#
# print("Letters", letters)
# print("Digits", digits)


##################TASK 14####################
# Write a Python program to check the validity of passwords.
#
# password = input("Enter password: ")
#
# if (6 <= len(password) <= 16
#         and any(c.islower() for c in password)
#         and any(c.isupper() for c in password)
#         and any(c.isdigit() for c in password)
#         and any(c in "$#@" for c in password)):
#
#     print("Valid password")
# else:
#     print("Invalid password") 