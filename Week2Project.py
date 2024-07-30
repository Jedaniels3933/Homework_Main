# User Interface Project   
def main():
    tasks = []
    while True:
        ans= input('''
"Welcome to the to-do list manager app!!!
Enter an option , please: 
1. Add a task
2. View All Tasks
3. Mark a Task as Complete 
4. Delete a Task
5. Exit                   
''')
        if ans == '1':
            value = input("Please enter a task: ")   
            tasks.append(value)
            print(f"Task {value} added successfully.")                 
        if ans == '2':  
            print("List of all tasks:")
            print(tasks[0:])     #display by slicing - Make this show numbers 1. 2. 
        if ans == '3':
            index = int(input("Which task would you like to mark as done ?: "))  
            if 0 < index <= len(tasks):
                tasks[index-1] = '{tasks[-1]}'
                print(f'Task {tasks.index[-1]} marked as complete.')     #CAnt man the string to XX help
                print(tasks)
        if ans == '4':
            index = int(input("Please enter the number of the task would you like to delete: "))   
            if 0 < index <= len(tasks):
                del tasks[index-1]     #Setting this as the default right ?? 
                print(f'Task {tasks[index[-1]]} deleted successfully.')  #Wont delete the task  #Type Error Help
            else:
                print("Please read the menu again and make a numerical choice .")      #This works Somehow??
            continue       
        if ans == '5':
            print("See  ya later aligator - Come back SOon!")          #This Works
            break

def add_task():
    task_name = input("Enter the task name: ")
    description = input("Enter the task description: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    tasks[task_name] = {'description': description, 'due_date': due_date, 'complete': False}
    print(f"Task {task_name} added successfully.")

          

    


main()     








      
       