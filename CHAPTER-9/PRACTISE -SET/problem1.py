f=open("poem.txt","r")
fdata=f.read()
if("Twinkle" in fdata):
    print("yes")

else:
    print("No")
