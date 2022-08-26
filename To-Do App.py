def ViewTask():
    tasks = open("Tasks.txt","r")
    print(tasks)
def AddTask():
    task_name=input("Type in the name of the task")
    task = open("Tasks.txt","a")
    task.write(task_name)
    print("Task Added!")
    ViewTasks=input("Would you like to see your pending tasks?")
    if ViewTasks==("No"):
        print("Ok.")
        exit()
    if ViewTasks==("Yes"):
        ViewTask()

    
        
    

    
    
