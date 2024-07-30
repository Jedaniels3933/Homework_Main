# User Interface Project   
tasks = ()
def main():
ans= input
{'''
"Welcome to the to-do list manager app!!!
Enter an option , please: 
1. Add a task
2. View All Tasks
3. Mark a Task as Complete 
4. Delete a Task
5. Exit                   
'''}
while tasks == True:
    if  ans == '1':
        add_task()

    elif ans == '2':
        view_tasks()
    elif ans == '3':
        mark_task_complete()
    elif ans == '4':
        delete_task()
    elif ans == '5':
        print("Thank you for using our app. Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")

def add_task():
    task_name = input("Enter the task name: ")
    description = input("Enter the task description: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    tasks[task_name] = {'description': description, 'due_date': due_date, 'complete': False}
    print(f"Task {task_name} added successfully.")
main()   

  
        

