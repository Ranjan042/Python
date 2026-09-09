# file = open("Quick-Revision/fileDemo.txt", "r")
# print(file.read())
# file.close

# with open("Quick-Revision/fileDemo.txt", "r") as file:
#     print(file.read())

# with open("Quick-Revision/fileDemo.txt", "r") as file:
#     for line in file:
#         print(line)

# with open ("Quick-Revision/Demo.py", "w") as file:
#     file.write('print("I am Written and created using python")')

# with open ("Quick-Revision/Demo.py", "r") as file:
#     print(file.read())

# with open ("Quick-Revision/Demo.py", "a") as file:
#     file.write('\nprint("I am appended using python")')

# try:
#      with open("Quick-Revision/New2.py", "x") as file:
#          pass
# except:
#     print("File Already Exists")
# else:
#     print("File Created Successfully")
# finally:
#     print("File Operation Completed")




for i in range(1,11):
    with open(f"Quick-Revision/TABLES/table{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i} * {j} = {i*j}\n")



