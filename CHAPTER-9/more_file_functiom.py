f=open("file.txt")

#print(lines)
#lines=f.readlines()  read all the lines
#print(type(lines))

#readline  read only one line at a time

# line1=f.readline()
# print(line1,type(line1))
# line2=f.readline()
# print(line2,type(line2))
# line3=f.readline()
# print(line3,type(line3))  #it can be done by using loop
# line4=f.readline()
# print(line4,type(line4))
line=f.readline()
while(line!=""):
    print(line,end="")
    line=f.readline()
f.close()