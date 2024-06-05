def main():
  tasks = []

  while True:
    print("\nTo-Do List:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      
      task = input("Enter a new task: ")
      tasks.append(task)
      print(f"Task '{task}' added!")
    elif choice == '2':
      if not tasks:
        print("There are no tasks in the list.")
      else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
          print(f"{i}. {task}")
    elif choice == '3':
      if not tasks:
        print("There are no tasks in the list.")
      else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
          print(f"{i}. {task}")
       
        task_num = int(input("Enter the number of the task to mark as done: ")) - 1
       
        if task_num < 0 or task_num >= len(tasks):
          print("Invalid task number.")
        else:
          del tasks[task_num]
          print("Task marked as done!")
    elif choice == '4':
      print("Exiting the To-Do List.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
