
a=int(input("Enter the value of A: "))
b=int(input("Enter the value of B: "))
c=int(input("Enter the value of c: "))

def greatestthree(a,b,c):
    if(a>b):
        if(a>c):
            print(f"{a} is greatest")
        else:
            print(f"{c} is greatest")
    else:
        if(b>c):
            print(f"{b} is greatest")
        else:
            print(f"{c} is greatest")

greatestthree(a,b,c)
    