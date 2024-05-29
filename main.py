import sqlite3

conn = sqlite3.connect('pydb.sqlite3')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY AUTOINCREMENT, task_name TEXT, details TEXT, status TEXT)''')

def add_task():
    task_name = input("Enter task name: ")
    details = input("Enter task details (optional): ")
    sql = "INSERT INTO tasks (task_name, details, status) VALUES (?, ?, ?)"
    val = (task_name, details, "Incomplete")
    cursor.execute(sql, val)
    conn.commit()
    print("Task added successfully.")

def delete_task():
    try:
        task_id = int(input("Enter task ID to delete: "))
        sql = "DELETE FROM tasks WHERE id = ?"
        val = (task_id,)
        cursor.execute(sql, val)
        conn.commit()
        print("Task deleted successfully.")
    except ValueError:
        print("Invalid ID. Please enter a number.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    if tasks:
        for task in tasks:
            print(f"ID: {task[0]}, Name: {task[1]}, Details: {task[2]}, Status: {task[3]}")
    else:
        print("No tasks found.")

def update_task():
    try:
        task_id = int(input("Enter task ID to update: "))
        new_details = input("Enter new details (leave blank to keep current): ")
        new_status = input("Enter new status (Incomplete/Complete): ").capitalize()
        sql = "UPDATE tasks SET details = ?, status = ? WHERE id = ?"
        cursor.execute(sql, (new_details, new_status, task_id))
        conn.commit()
        print("Task updated successfully.")
    except ValueError:
        print("Invalid ID. Please enter a number.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Update Task")
    print("5. Exit")

    choice = input("Enter your choice:\n ")

    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        update_task()
    elif choice == "5":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")

cursor.close()
conn.close()
