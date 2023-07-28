import sqlite3
import tkinter as tk
from tkinter import messagebox
import random


def bot_response(user_input):
    user_input = user_input.strip().lower()

    if user_input == "help":
        return """Available commands:
        - add <task description>: Add a new task.
        - view: View all tasks.
        - complete <task_id>: Mark a task as completed.
        - delete <task_id>: Delete a task.
        - help: Show available commands.
        - exit: Exit the app."""

    elif user_input == "exit":
        # Return None to indicate the app should exit
        return None

    elif user_input.startswith("add "):
        # Extract the task description after "add " and add it to the ToDo list
        task_description = user_input[4:].strip()
        if task_description:
            # Add the task to the SQLite database
            connection = sqlite3.connect("tasks.db")
            cursor = connection.cursor()

            cursor.execute("INSERT INTO tasks (description) VALUES (?)", (task_description,))
            connection.commit()
            connection.close()

            return f"Task added: {task_description}"
        else:
            return "Please provide a task description after 'add' command."

    elif user_input == "view":
        # Retrieve all tasks from the database and format them for display
        connection = sqlite3.connect("tasks.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        connection.close()

        if tasks:
            tasks_list = "\n".join(f"{task[0]}. {task[1]}" for task in tasks)
            return f"Tasks:\n{tasks_list}"
        else:
            return "No tasks found."

    elif user_input.startswith("complete "):
        # Mark the task as completed based on the provided task_id
        task_id = user_input[9:].strip()
        if task_id.isdigit():
            connection = sqlite3.connect("tasks.db")
            cursor = connection.cursor()

            cursor.execute("UPDATE tasks SET is_completed = 1 WHERE id = ?", (task_id,))
            connection.commit()
            connection.close()

            return f"Task {task_id} marked as completed."
        else:
            return "Please provide a valid task_id after 'complete' command."

    elif user_input.startswith("delete "):
        # Delete the task based on the provided task_id
        task_id = user_input[7:].strip()
        if task_id.isdigit():
            connection = sqlite3.connect("tasks.db")
            cursor = connection.cursor()

            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            connection.commit()
            connection.close()

            return f"Task {task_id} deleted."
        else:
            return "Please provide a valid task_id after 'delete' command."

    else:
        return "I'm just a simple bot. I can't process that command. Type 'help' to see the available commands."

def create_table():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            is_completed INTEGER DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo App")
        # Initialize any data structures or variables for tasks here.

        # Call methods to create the GUI elements.
        self.create_widgets()

    def create_widgets(self):
        self.task_label = tk.Label(self.root, text="Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(self.root, width=40)
        self.tasks_listbox.pack()

        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        # Populate the listbox with tasks from data structures (if any).
        # For example:
        # for task in self.tasks:
        #     self.tasks_listbox.insert(tk.END, task)

            # Populate the listbox with tasks from the database.
        connection = sqlite3.connect("tasks.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        for task in tasks:
            self.tasks_listbox.insert(tk.END, task[1])

        connection.close()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            connection = sqlite3.connect("tasks.db")
            cursor = connection.cursor()

            cursor.execute("INSERT INTO tasks (description) VALUES (?)", (task,))
            connection.commit()
            connection.close()

            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def complete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            selected_task = self.tasks_listbox.get(selected_index)
            connection = sqlite3.connect("tasks.db")
            cursor = connection.cursor()

            cursor.execute("UPDATE tasks SET is_completed = 1 WHERE description = ?", (selected_task,))
            connection.commit()
            connection.close()

            self.tasks_listbox.itemconfig(selected_index, {'bg': 'light green'})

    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            selected_task = self.tasks_listbox.get(selected_index)
            connection = sqlite3.connect("tasks.db")
            cursor = connection.cursor()

            cursor.execute("DELETE FROM tasks WHERE description = ?", (selected_task,))
            connection.commit()
            connection.close()

            self.tasks_listbox.delete(selected_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

