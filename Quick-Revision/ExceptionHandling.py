# Synta Errors
# print("Hello world)

# Indentation ErrorR
# if 0==0:
# print("Hello world")


# """# Run Time Errors(Exceptions or Exceptions)
# ZeroDivisionError
# 1/0

# NameError
# print(a)

# IndexError
# a=[1,2,3,4]
# print(a[5])

# KeyError
# d={"a":1,"b":2}
# print(d["c"])

# AttributeError
# a=10
# print(a.upper())

# TypeError
# a=10
# print(a+10)

# def func(a,b):
#     return a/b
# print(func(10,0)) #cause ZeroDivisionError"""

# def func(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Cannot divide by zero")

# print(func(10,0))

# def checkVoterWithAge(age):
#     if age>=18:
#         print("You are eligible to vote")
#     else:
#         raise Exception("You are not eligible to vote")

# age=int(input("Enter your age: "))
# checkVoterWithAge(age)


try:
    a = int(input("Enter number: "))
    b = 10 / a

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", b)

finally:
    print("Program execution completed")


