with open("donkey.txt","r") as f:
    data=f.read()

newdata=data.replace("donkey","#####")

with open("donkey.txt","w") as f:
    f.write(newdata)