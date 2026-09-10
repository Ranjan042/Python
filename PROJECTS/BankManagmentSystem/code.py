import json

class BankAccount:
    def __init__(self,username,password,balance,pin):
        self.username=username
        self.__password=password
        self.__balance=balance
        self.__pin=pin


    def setBalance(self,balance):
        self.__balance=balance

    def getBalance(self):
        return self.__balance

    def comparePin(self,pin):
        return self.__pin==pin

    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        self.__balance-=amount

    def transfer(self,amount,receiver):
        self.withdraw(amount)
        receiver.deposit(amount)

    def display(self):
        print(f"Name:{self.username}")
        print(f"Balance:{self.__balance}")
        print(f"Pin:{self.__pin}")

def ReadData():
    with open("PROJECTS/BankManagmentSystem/data.json","r") as file:
     data=json.load(file)

    return data or []

def WriteData(data):
    with open("PROJECTS/BankManagmentSystem/data.json","w") as file:
     json.dump(data,file)

def showDashboard(account):
      while(True):
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Transfer")
        print("4.Dashboard")
        print("5.Logout")
        choice=int(input("Enter your choice:"))
        if(choice==1):
            amount=int(input("Enter the amount:"))
            HandleDeposit(account,amount)
        elif(choice==2):
            amount=int(input("Enter the amount:"))
            pin=int(input("Enter your pin:"))
            HandleWithdraw(account,amount,pin)
        elif(choice==3):
            amount=int(input("Enter the amount:"))
            receiver=input("Enter the receiver name:")
            pin=int(input("Enter your pin:"))
            HandleTransfer(account,amount,receiver,pin)
        elif(choice==4):
            account.display()
        elif(choice==5):
            break

def handleLogin():

    username=input("Enter your username:")
    password=input("Enter your password:")
    data=ReadData()
    for i in range(len(data)):
        if(data[i]["username"]==username and data[i]["password"]==password):
            print("Login successful")
            account=BankAccount(username,password,data[i]["balance"],data[i]["pin"])
            showDashboard(account)
            break
    else:
        print("Invalid username or password")

def HandleRegister():
    username=input("Enter your username:")
    password=input("Enter your password:")
    pin=int(input("Enter your pin:"))
    data=ReadData()
    for i in range(len(data)):
        if(data[i]["username"]==username):
            print("Username already exists")
            return
    else:
        data.append({"username":username,"password":password,"balance":0,"pin":pin})
        WriteData(data)
        print("Registration successful")

def HandleDeposit(account,amount):
    data=ReadData()
    for i in range(len(data)):
        if(data[i]["username"]==account.username):
            account.deposit(amount)
            data[i]["balance"]+=amount
            WriteData(data)
            print("Deposit successful")
            break

def HandleWithdraw(account,amount,pin):
    data=ReadData()
    currBalance=account.getBalance()
    if(currBalance<amount):
        print("Insufficient balance")
    else:
        for i in range(len(data)):
            if(data[i]["username"]==account.username and account.comparePin(pin)):
                account.withdraw(amount)
                data[i]["balance"]-=amount
                WriteData(data)
                print("Withdrawal successful")
                break

def HandleTransfer(account, amount, receiver, pin):
    data = ReadData()

    if account.username == receiver:
        print("You cannot transfer to yourself")
        return

    if not account.comparePin(pin):
        print("Invalid PIN")
        return

    if account.getBalance() < amount:
        print("Insufficient balance")
        return

    sender = next(
        (i for i in data if i["username"] == account.username),
        None
    )

    receiver_account = next(
        (i for i in data if i["username"] == receiver),
        None
    )

    if receiver_account is None:
        print("Receiver not found")
        return

    sender["balance"] -= amount
    receiver_account["balance"] += amount

    account.setBalance(sender["balance"])

    WriteData(data)

    print("Transfer successful")
        
def main():
    print("Bank Management System")
    print("1.Login")
    print("2.Register")
    choice=int(input("Enter your choice:"))

    if(choice==1):
        handleLogin()  
    if(choice==2):
        HandleRegister()

# ReadData()
main()
    