# To Do List By A.ulrhman

# Data 

tasks = ["Take a showe", "Make my bed"]

# Functions

def view_tasks():
    for count, task in enumerate(tasks, 1):
        print(count, task)

def add_task():
    while True:
        task = input("What task do you want to add? ")
        tasks.append(task.title())
        again = input("Add another task? (y/n): ")
        if again.lower() == "n":
            break


def complete_task():
    view_tasks()
    complete = int(input("Type The Task Number : "))
    if 1 <= complete <= len(tasks):
        tasks.pop(complete - 1)
        print("Done - Keep Going.")
    else:
        print("[X] Invalid number!")




def delete_task():
    view_tasks()
    delete = int(input("Type The Task Number: "))
    if 1 <= delete <= len(tasks):
        tasks.pop(delete - 1)
        print("Done.")
    else:
        print("[X] Invalid number!")


def main():
    while True:
        print("""
        Welcome To My To-Do-List App
        [ 1 ] Add Task
        [ 2 ] Complete Task
        [ 3 ] View Tasks
        [ 4 ] Delete Task
        [ 5 ] Exit
        """)
        try:
            choice = int(input("Choice A Number: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                complete_task()
            elif choice == 3:
                view_tasks()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                exit()
        except ValueError:
            print("[X] Enter a valid number!\n")


main()





