num1=int(input("Enter first Number"))
num2=int(input("Enter second Number"))
num3=int(input("Enter third Number"))
num4=int(input("Enter fourth Number"))

if(num1>num2 and num1>num3 and num1>num4):
    print("Num1 is greater")

if(num2>num1 and num2>num3 and num2>num4):
    print("Num2 is greater")

if(num3>num2 and num3>num1 and num3>num4):
    print("Num3 is greater")

if(num4>num2 and num4>num3 and num4>num1):
    print("Num4 is greater")
