with open("flog.txt") as f:
    data=f.read()

if("python" in data):
    print("yes it contains python")
else:
 print("It not contain the word python")