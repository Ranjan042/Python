marks1=int(input("Enter your marks in math: "))
marks2=int(input("Enter your marks in physics: "))
marks3=int(input("Enter your marks in Biology: "))

percentage=(marks1+marks2+marks3)/3

if(marks1>34 and marks2>34 and marks3>34):
    if(percentage>=40):
        print("You are passed")
    else:
        print("Your are Fail")
else:
    print("You are fail")