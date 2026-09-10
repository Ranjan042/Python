# #OOPS(create classes and objects,access class attributes and methods)

# class Car:
#     brand="Toyota" #class variable or static variable or Attribute
#     def __init__(self,name,year): #constructor
#         self.name=name #instance variable
#         self.year=year

#     def drive(self):
#         print(f"{self.name} is driving")

#     def stop(self):
#         print(f"{self.name} is stopped")

# #Directly Accessing Class Attributes
# print(Car.brand)



# car1=Car("Toyota",2022)
# print(car1.brand)
# print(car1.name)
# print(car1.year)
# car1.drive()
# car1.stop()

# car2=Car("Honda",2023)
# print(car2.brand)
# print(car2.name)
# print(car2.year)
# car2.drive()
# car2.stop()

#Constructor

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age  
#     def display(self):
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")

# student1=Student("Ranjan",20) 
# # A constructor is a method that runs automatically when we
# # call a class and this constructor function will target the
# # objects location
# student1.display()


#Attributes and Methods

# class attribut: A normal variable that belongs to a class
# instance attribute: A variable that belongs to an instance of a class

# class Car:
#     wheels=4 #class attribute
#     def __init__(self,name,color):
#         self.name=name #instance attribute
#         self.color=color #instance attribute



#Instance Method- A method that belongs to an instance of a class

# class Car:
#     wheels=4 #class attribute

#     @classmethod
#     def classmethod(cls):
#         print("This is a class method")

#     @staticmethod
#     def staticmethod():
#         print("This is a static method")

#     def __init__(self,name,color):
#         self.name=name #instance attribute
#         self.color=color #instance attribute
#     def drive(self):#instance method  
#         print(f"{self.name} is driving")

# Car.classmethod()
# Car.staticmethod()

#Inheritance

# class Parent:
#     def __init__(self,name):
#         self.name=name

#     def parentMethod(self):
#         print("Parent method")

#     def childMethod(self):
#         print("Child method in parent class")

#     def spendMoney(self):
#         print("I can Spend money")


# class Child(Parent):
#     def __init__(self,name):
#         super().__init__(name)

#     def childMethod(self):
#         print("Child method")

#     def display(self):
#         print(f"Name:{self.name}")

# c1=Child("Sonu")
# c1.parentMethod()
# c1.childMethod()
# c1.spendMoney()
# c1.display()

#Type of Inheritance
#Single inheritance
#Multiple inheritance
#Multilevel inheritance


#Single Inheritance

# class A:
#     pass

# class B(A):
#     pass

#Multiple Inheritance

# class A:
#     pass

# class B:
#     pass

# class C(A,B):
#     pass

#Multilevel Inheritance

# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

#POLYMORPHISM

#Method Overloading python does not support method overloading
# class Sum:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c

# sum1=Sum()
# print(sum1.add(1,2))
# print(sum1.add(1,2,3))


#Method Overriding

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# animal=Animal()
# animal.sound()

# dog=Dog()
# dog.sound()

#Duck Typing

# Duck typing means that:
# An object's type/class is less important than what it can do

# Python follows the idea:
# "If it walks like a duck and quacks like a duck, treat it like a duck."

# class Dog:
#     def sound(self):
#         print("Bark")


# class Cat:
#     def sound(self):
#         print("Meow")

# class Silent:
#     pass


# def make_sound(animal):
#     animal.sound()


# make_sound(Dog())
# make_sound(Cat())
# make_sound(Silent())

#Encapsulation and Access Modifiers

# class Demo:
#     def __init__(self,name):
#         self.name="Public Member"
#         self._protected="Protected Member"
#         self.__private="Private Member"

#     def display(self):
#         print("Inside the class: Demo ")
#         print(f"Name:{self.name}")
#         print(f"Protected:{self._protected}")
#         print(f"Private:{self.__private}")

# demo=Demo("Ranjan")
# demo.display()

# print("Outside the class")
# print(f"Name:{demo.name}")
# print(f"Protected:{demo._protected}") #it is accessible,because it is just naming convention to tell developers
# # print(f"Private:{demo.__private}") it is not accessible

#Abstraction
#Abstraction is the process of hiding the implementation details and showing only the necessary information to the user,but in python it is not supported
#We can using library to achieve abstraction