# todo.py

def show_menu():
    print("\n to-do list menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

def read_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []


def write_tasks(tasks):
   with open("tasks.txt","w") as file:
      for task in tasks:
         file.write(task + "\n")   
def view_tasks():
    tasks = read_tasks()
    if not tasks:
       print("No tasks yet!")
    else:
       print("Your tasks: ")           
       for i, task in enumerate(tasks, start=1):
          print(f"{i}.{task}")
def add_task():
   task = input("Enter new task: ")  
   tasks = read_tasks()
   tasks.append(tasks)       
   write_tasks(task)
   print("Task added!")

def delete_task():
    tasks = read_tasks()
    view_tasks()
    try:
        index = int(input("❌ Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            write_tasks(tasks)
            print(f"🗑 Task '{removed}' deleted!")
        else:
            print("⚠ Invalid task number!")
    except ValueError:
        print("❌ Please enter a number!")

 # Main loop
while True:
   show_menu()
   choice = input("Choose (1-4): ")
   if choice == "1":
      view_tasks()
   elif choice == "2":
      add_task()
   elif choice == "3":
      delete_task()
   elif choice == "4":
      print("Goodbye!")
      break
   else:
      print("Invalid choice, try again.")                   