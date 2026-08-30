animal=["donkey","monkey","lion","tiger"]

with open("donkey2.txt","r") as f:
    data=f.read()

for item in animal:
      data=data.replace(item,"#" * len(item))

with open("donkey2.txt","w") as f:
    f.write(data)