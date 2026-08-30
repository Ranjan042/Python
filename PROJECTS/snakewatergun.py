import random
computer=random.choice([-1,1,0])
# print(computer)

player=input("Enter your choice s(snake),w(water),g(gun): ")
dict={"s":-1,"w":1,"g":0}
reversdict={-1:"snake",1:"water",0:"gun"}

you = dict[player]
print(f"you choose:{reversdict[you]}\ncomputer choose: {reversdict[computer]}")
if(computer==you):
    print("Draw!")
elif(computer==-1 and you==1):
    print("Computer Wins!")
elif(computer==-1 and you==0):
    print("You wins!")
elif(computer==1 and you==-1):
    print("Computer wins!")
elif(computer==1 and you==0):
    print("computer wins!")
elif(computer==0 and you==-1):
    print("computer wins!")
elif(computer==0 and you==1):
    print("You wins")
