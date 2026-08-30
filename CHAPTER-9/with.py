# f=open("file.txt")
# print(f.read())
# f.close it can be written using with statement like this

with open("file.txt") as f:
    print(f.read())

    # you dont have to axplixitly close the file