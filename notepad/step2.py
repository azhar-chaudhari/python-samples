import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter.simpledialog import askstring

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

def find_text():
    if not hasattr(find_text, 'dialog'):
        find_text.dialog = tk.Toplevel(window)
        find_text.dialog.title("Find")
        
        find_label = tk.Label(find_text.dialog, text="Find:")
        find_label.pack(side=tk.LEFT)
        
        find_entry = tk.Entry(find_text.dialog, width=30)
        find_entry.pack(side=tk.LEFT)
        find_entry.focus_set()
        
        def find_next():
            search_text = find_entry.get()
            start_pos = text.search(search_text, tk.END, regexp=True)
            if start_pos:
                text.tag_remove('found', '1.0', tk.END)
                while start_pos:
                    end_pos = start_pos + f"+{len(search_text)}c"
                    text.tag_add('found', start_pos, end_pos)
                    text.tag_config('found', background='blue', foreground='white')
                    start_pos = text.search(search_text, end_pos, tk.END, regexp=True)
                text.focus_set()
            else:
                messagebox.showinfo("Find", "Text not found.")
        
        find_button = tk.Button(find_text.dialog, text="Find Next", command=find_next)
        find_button.pack(side=tk.LEFT)
        
        def close_find_dialog():
            text.tag_remove('found', '1.0', tk.END)
            find_text.dialog.destroy()
            del find_text.dialog
        
        close_button = tk.Button(find_text.dialog, text="Close", command=close_find_dialog)
        close_button.pack(side=tk.LEFT)

def replace_text():
    replace_dialog = tk.Toplevel(window)
    replace_dialog.title("Replace")
    
    find_label = tk.Label(replace_dialog, text="Find:")
    find_label.pack(side=tk.LEFT)
    
    find_entry = tk.Entry(replace_dialog, width=30)
    find_entry.pack(side=tk.LEFT)
    find_entry.focus_set()
    
    replace_label = tk.Label(replace_dialog, text="Replace with:")
    replace_label.pack(side=tk.LEFT)
    
    replace_entry = tk.Entry(replace_dialog, width=30)
    replace_entry.pack(side=tk.LEFT)
    
    def replace_next():
        search_text = find_entry.get()
        replace_text = replace_entry.get()
        start_pos = text.search(search_text, tk.END, regexp=True)
        if start_pos:
            text.delete(start_pos, start_pos + f"+{len(search_text)}c")
            text.insert(start_pos, replace_text)
            text.tag_remove('found', '1.0', tk.END)
            text.focus_set()
        else:
            messagebox.showinfo("Replace", "Text not found.")
    
    replace_button = tk.Button(replace_dialog, text="Replace Next", command=replace_next)
    replace_button.pack(side=tk.LEFT)
    
    def close_replace_dialog():
        text.tag_remove('found', '1.0', tk.END)
        replace_dialog.destroy()
    
    close_button = tk.Button(replace_dialog, text="Close", command=close_replace_dialog)
    close_button.pack(side=tk.LEFT)

def select_font():
    font_name = askstring("Select Font", "Enter the font name:")
    if font_name:
        if font_name in tkfont.families():
            text.configure(font=(font_name, 12))
        else:
            messagebox.showerror("Font Error", f"The font '{font_name}' does not exist on your system.")

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

# Create the Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=False)
edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: text.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: text.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: text.event_generate("<<Paste>>"))
edit_menu.add_separator()
edit_menu.add_command(label="Find", command=find_text)
edit_menu.add_command(label="Replace", command=replace_text)

# Add the Edit menu to the menu bar
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Create the Font menu
font_menu = tk.Menu(menu_bar, tearoff=False)

# Get the list of system fonts
system_fonts = tkfont.families()

# Add each font to the Font menu
for font in system_fonts:
    font_menu.add_command(label=font, command=lambda font=font: text.configure(font=(font, 12)))

# Add the Font menu to the menu bar
menu_bar.add_cascade(label="Font", menu=font_menu)

# Configure the window to use the menu bar
window.config(menu=menu_bar)

# Start the main loop
window.mainloop()
