with open("flog.txt","r") as f:
    lines=f.readlines()

lineno=1
for line in lines:  
   if("python" in line):
    print(f"python is present in the line:{lineno}")
    lineno+=1

else:
   print("not present")