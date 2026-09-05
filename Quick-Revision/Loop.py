# # Loop in Python for Numbers
# for i in range(10):
#     print(i)

# for i in range(1, 11):
#     print(i)

# for i in range(1, 11, 2):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# # while True:
# #     print("This is an infinite loop")

# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1

# #Loop in Python for Strings

# a="Nature"
# for char in a:
#     print(char)

# for i in range(len(a)):
#     print(a[i])

# for i in range(len(a)-1,-1,-1):
#     print(a[i])

# #Loop in Python for Lists

# a=[1,2,3,4,5]
# for num in a:
#     print(num)

# for i in range(len(a)):
#     print(a[i])

# for i in range(len(a)-1,-1,-1):
#     print(a[i])

# #Break and Continue in Python
# for i in range(10):
#     if i==5:
#         break
#     print(i)

# for i in range(10):
#     if i==5:
#         continue
#     print(i)

# for i in range(10):
#     if i==5:
#         pass
#     print(i)

# pass = do nothing and continue execution.

# #Nested Loop in Python
# for i in range(3):
#     for j in range(3):
#         print(i,j)

#else in Loop in Python
# for i in range(5):
#     print(i)
# else:
#     print("Loop is completed")

# Accept an integer and Print hello world n time
# count=int(input("Enter the number of times to print hello world: "))
# for i in range(count):
#     print("Hello World",i+1,"times")

# Factorial of a number using for loop
# n=int(input("Enter a number to find its factorial:"))
# f=1
# for i in range(1,n+1,1):
#     f=f*i
# print("Factorial of",n,"is",f)

# Count all letters, digits, and special symbols from a given 
# string 
# Given: str1 = "P@#yn26at^&i5ve" 
# Expected Outcome: 
# Total counts of chars, digits, and symbols 
# Chars = 8 
# Digits = 3 
# Symbol = 4

# str1 = "P@#yn26at^&i5ve"
# chars=0
# digits=0
# symbols=0

# for char in str1:
#     if char.isalpha():
#         chars+=1
#     elif char.isdigit():
#         digits+=1
#     else:
#         symbols+=1

# print("Chars=",chars)
# print("Digits=",digits)
# print("Symbols=",symbols)

#Random number guessing game

import random
num=random.randint(1,100)

while True:
    guess=int(input("Enter a number between 1 and 100: "))
    if guess==num:
        print("You guessed it!")
        break
    elif guess<num:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")

