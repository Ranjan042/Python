tasks=[]
# task=input("Enter your task")
# tasks.append(task)
# print(tasks[0])

def display():
    print("Welcome to my to do list")
    print("1.Add Task")
    print("2.Viwe Task")

def add(tasks):
    task=input("Enter your task")
    tasks.append(task)

def printt(tasks):
    for item in tasks:
        print(item)

while(True):
  display()
  choice=int(input("your choice"))
  if(choice==1):
      add(tasks)
  elif(choice==2):
      printt(tasks)