# Built in ds
# 1.List
# 2.Tuple
# 3.Set
# 4.Dictionary

# 1.List
# List is a collection which is ordered and changeable. Allows duplicate members

# list=[1,2,3,4,5,5,5,5,"ranjan",None,True,[1,2,3],(1,2,3)]
# print(list)
# list[0]=10
# print(list)
# # for elem in list:
# #     print(elem)
# for i in range(len(list)):
#     print(list[i])


# 2.Tuple
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members

# tuple=(1,2,3,4,5,5,5,5,"ranjan",None,True,[1,2,3],(1,2,3))
# print(tuple)
# for elem in tuple:
#     print(elem)
# tuple[0]=10 // tuple is immutable
# for i in range(len(tuple)):
#     print(tuple[i])


# 3.Set
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members

# set={1,2,3,4,5,5,5,5,"ranjan",None,True,(1,2,3)}
# print(set)
# for elem in set:
#     print(elem)
# print(set.pop())
# print(5 in set)
# print(set.clear())


# 4.Dictionary
# Dictionary is a collection which is ordered* and changeable. No duplicate members

# dict={1:"a",2:"b",3:"c",4:"d"}
# print(dict)
# print(dict[1])
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# dict[1]="A"
# dict[5]="E"
# dict.update({2:"B"})
# print(dict)


# 1. List []

# append()      # add at end
# extend()      # add multiple elements
# insert()      # add at index
# remove()      # remove by value
# pop()         # remove by index
# clear()       # remove all
# index()       # find index of value
# count()       # count occurrences
# sort()        # sort
# reverse()     # reverse
# 2. Tuple ()
# count()       # count occurrences
# index()       # find index

# Tuple is immutable, so it has fewer methods.

# 3. Set {}
# add()         # add element
# update()      # add multiple elements
# remove()      # remove element
# discard()      # remove element without error
# pop()         # remove random element
# clear()       # remove all
# union()
# intersection()
# difference()
# symmetric_difference()

# 4. Dictionary {key: value}
# get()         # get value
# keys()        # get all keys
# values()      # get all values
# items()       # get key-value pairs
# update()      # add/update key-value
# pop()         # remove key
# popitem()     # remove last key-value pair
# clear()       # remove all

# 5. String ""
# upper()
# lower()
# capitalize()
# title()
# strip()
# replace()
# split()
# join()
# find()
# index()
# count()
# startswith()
# endswith()

# Print positive and negative elements of an List?

# list=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
# print("Positive element are :",end=" ")
# for elem in list:
#     if elem>0:
#         print(elem,end=" ")

# print()

# print("Negative elemnts are: ",end=" ")
# for elem in list:
#     if(elem<0):
#         print(elem,end=" ")

# Find the second greatest element?

# list=[1,2,5,6,8,4,3,9,15,6,15,17,16]

# first=-999
# second=-999

# for elem in list:
#     if elem>first:
#         second=first
#         first=elem
#     elif second<elem and second<=first:
#         second=elem

# print(second)

# Write a Python program to sum all the values in a dictionary?

# dict={"a":5,"b":10}

# sum=0

# for item in dict:
#     sum+=dict[item]

# print(sum)

# Write a Python script to merge two Python dictionaries?

# dict1={"a":5,"b":10,"c":15}
# dict2={"d":5,"e":10,"f":15}

# ans={}

# for i in dict1:
#     ans[i]=dict1[i]

# for i in dict2:
#     ans[i]=dict2[i]

# print(ans)
