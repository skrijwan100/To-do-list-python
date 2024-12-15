import json
mytask=[]
def add_task():
   task=input("Enter your task:")
   mytask.append(task)
   print("Your task is successfully add.")
def viwe_task():
    for no,i in enumerate(mytask):
        no+=1
        print(f"{no}. {i}")
def delete_task():
    for no,i in enumerate(mytask):
        no+=1
        print(f"{no}. {i}")
    user_delete=int(input("Enter the task index you want to delete:"))-1
    del_task=mytask.pop(user_delete)
    print(f"successfully delete  {del_task} task.")
    
def save_task():
    with open("MY_task.txt","w") as file:
         for no,i in enumerate(mytask):
            no+=1
            file.write(f"{no}. {i}\n")
    print("file load done.")
def marks_com():
        for no,i in enumerate(mytask):
          no+=1
          print(f"{no}. {i}")
        user_com=int(input("which task is complected? enter his index:"))-1
        mytask.insert(user_com,f"{mytask[user_com]} complected")
        mytask.remove(mytask[user_com+1])

def load_file():
    global mytask
    userfile = input("Enter the file name:")
    with open(f"{userfile}.txt","r") as file:
        mytask=json.load(file)


while True:
    try:
        if(__name__=="__main__"):
            print('''Choose your optinon ....
                1.add task
                2.viwe all task
                3.Marks task as complected
                4.Delete a task
                5.Save task to a file
                6.load a task form file
                7.exit
            ''')
            user=int(input("Enter your Choose:"))
            if user==1:
                add_task()
            elif user==2:
                viwe_task()
            elif user==3:
                marks_com()
            elif user==4:
                delete_task()
            elif user==5:
                save_task()
            elif user==6:
               load_file()
            elif user==7:
               exit()
    except Exception as e:
        print(e)
        # print("you enter a invaid input.\n Enter the index number of choose task.")
    


