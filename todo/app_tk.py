import tkinter as tk
from tkinter import ttk
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Create the todo table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
''')
conn.commit()


def create_task():
    """
    Create a new task.
    """
    task_name = entry_task.get()
    cursor.execute("INSERT INTO todos (task) VALUES (?)", (task_name,))
    conn.commit()
    lbl_status.config(text="Task created successfully!")
    entry_task.delete(0, tk.END)
    read_tasks()


def read_tasks():
    """
    Read all tasks.
    """
    cursor.execute("SELECT * FROM todos")
    tasks = cursor.fetchall()
    task_list.delete(*task_list.get_children())
    for task in tasks:
        task_id, task_name, completed = task
        status = "Done" if completed else "Not done"
        task_list.insert("", tk.END, values=(task_id, task_name, status))


def update_task():
    """
    Update a task.
    """
    selected_item = task_list.focus()
    if selected_item:
        task_id = task_list.item(selected_item)['values'][0]
        task_name = entry_task.get()
        cursor.execute("UPDATE todos SET task = ? WHERE id = ?", (task_name, task_id))
        conn.commit()
        lbl_status.config(text="Task updated successfully!")
        entry_task.delete(0, tk.END)
        read_tasks()
    else:
        lbl_status.config(text="No task selected.")


def delete_task():
    """
    Delete a task.
    """
    selected_item = task_list.focus()
    if selected_item:
        task_id = task_list.item(selected_item)['values'][0]
        cursor.execute("DELETE FROM todos WHERE id = ?", (task_id,))
        conn.commit()
        lbl_status.config(text="Task deleted successfully!")
        read_tasks()
    else:
        lbl_status.config(text="No task selected.")


# Create the main window
window = tk.Tk()
window.title("Todo App")

# Create the task list
task_list = ttk.Treeview(window, columns=("ID", "Task", "Status"), show="headings")
task_list.heading("ID", text="ID")
task_list.heading("Task", text="Task")
task_list.heading("Status", text="Status")
task_list.pack(padx=10, pady=10)

# Create the task entry
entry_task = ttk.Entry(window, width=30)
entry_task.pack(padx=10)

# Create buttons
frame_buttons = ttk.Frame(window)
frame_buttons.pack(pady=5)
btn_create = ttk.Button(frame_buttons, text="Create Task", command=create_task)
btn_create.grid(row=0, column=0, padx=5)
btn_update = ttk.Button(frame_buttons, text="Update Task", command=update_task)
btn_update.grid(row=0, column=1, padx=5)
btn_delete = ttk.Button(frame_buttons, text="Delete Task", command=delete_task)
btn_delete.grid(row=0, column=2, padx=5)

# Create status label
lbl_status = ttk.Label(window, text="", foreground="blue")
lbl_status.pack(pady=5)

# Read and display initial tasks
read_tasks()

# Start the main loop
window.mainloop()

# Close the database connection
conn.close()
