li=["ranjan","mithun","hariom","Kishor"]
given_name=input("Enter your name: ")

if(given_name in li):
    print("{} is Present in the list".format(given_name))
    # print("%s is present in the list"% given_name)
else:
    print(f" {given_name} is Not present")

