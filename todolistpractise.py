import json
import os

FILENAME="dataload2.json"


if os.path.exists(FILENAME):
   with open(FILENAME,'r') as f:
    data=json.load(f)
    to_do_list=data.get("to_do_list",[])
    completed_list=data.get("completed_list",[])

else:

 to_do_list=[]
 completed_list=[]

def add_task():
        category=input("enter your task here: ")
        time=input("Enter the time you want to perform the task:")
        due_task= {'category':category, 'time':time}
        to_do_list.append(due_task)
        print("Task added sucessfully!!")
        save_data()

def view_task():
        if len(to_do_list)>0:
         for index,tasks in enumerate(to_do_list):
            print(f"{index}:{tasks}")
        else:
           print("empty task!!")


def mark_done():
        view_task()
        try:
         done=int(input("enter the task you want to delete:"))
         if 0 <= done < len(to_do_list):        
          completed_tasks= to_do_list.pop(done)
          print("task sucessfully removed!!")
          completed_list.append(completed_tasks)
          save_data()
         else:
            print("no task selected!!")
        except ValueError:
            print("enter a number!!")

def view_completed_tasks():
        for comp in completed_list:
            print(comp)

def save_data():
    data={

        'to_do_list':to_do_list,
        'completed_list':completed_list
    }
    with open(FILENAME, "w") as f:
        json.dump(data,f,indent=4)



while True:

    print("--Menu--")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark tasks as done")
    print("4. View completed tasks")
    print("5. Quit")

    try:
        choice=int(input("Enter the task you want to perform:"))
    except:
        print("sorry its invalid choice!!")
        continue   
    
    if choice==1:
        add_task()

    elif choice==2:
        view_task()

    elif choice==3:
        mark_done()

    elif choice==4:
        view_completed_tasks()

    elif choice==5:
        break

