#!/usr/bin/env python3
# coding=utf-8

# To-Do List application that allows users to add and view tasks

print(" TO-DO LIST APP ".center(40, "="))
todo_list = []

while True:
    print("\n" + "-" * 40)
    print("1. Add Task to the application")
    print("2. View Tasks")
    print("3. Exit")
    print("-" * 60)

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("\n--- Add Task ---")
        task = input("Enter a new task: ")
        todo_list.append(task)
        print("Task added successfully")


    elif choice == "2":
        print("\n--- Your Tasks ---")
        if len(todo_list) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("\nThank you for using the To-Do List")
        break

    else:
        print("Invalid choice!")

        if choice != "3":
            back = input("\nPress Enter to return to the menu...")
