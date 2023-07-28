import tkinter as tk
from tkinter import filedialog

def new_file():
    text.delete('1.0', tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete('1.0', tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = current_file_path.get()
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', tk.END))
    else:
        save_file_as()

def save_file_as():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', tk.END))
            current_file_path.set(file_path)

def close_app():
    window.destroy()

window = tk.Tk()
window.title("Notepad App")

current_file_path = tk.StringVar()

# Create the text area
text = tk.Text(window)
text.pack(fill=tk.BOTH, expand=True)

# Create the menu bar
menu_bar = tk.Menu(window)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=False)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Close", command=close_app)

# Add the File menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure the window to use the menu bar
window.config(menu=menu_bar)

# Start the main loop
window.mainloop()
