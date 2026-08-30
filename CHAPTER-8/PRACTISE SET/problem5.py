n=int(input("Enter number of lines: "))

def printstar(n):
    for i in range(0,n):
        print("*" *(n-i) )
printstar(n)