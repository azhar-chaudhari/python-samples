import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
import webbrowser
import tkinter.colorchooser as colorchooser
from bs4 import BeautifulSoup, Tag
from pygments import lex
from pygments.lexers import HtmlLexer
from pygments.styles import get_style_by_name

def new_file():
    text.delete('1.0', tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('HTML Files', '*.html')])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete('1.0', tk.END)
            text.insert(tk.END, file.read())
        parse_html()

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.html', filetypes=[('HTML Files', '*.html')])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', tk.END))
        messagebox.showinfo("Save", "File saved successfully.")

def preview():
    temp_file = 'temp.html'
    with open(temp_file, 'w') as file:
        file.write(text.get('1.0', tk.END))
    webbrowser.open(temp_file)

def close_app():
    if messagebox.askyesno("Close", "Are you sure you want to exit?"):
        window.destroy()

def insert_tag():
    selected_tag = tag_var.get()
    if selected_tag:
        start = text.index(tk.INSERT)
        text.insert(tk.INSERT, f"<{selected_tag}>")
        end = text.index(tk.INSERT)
        text.tag_add(selected_tag, start, end)
        text.tag_config(selected_tag, foreground=color_var.get())

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        color_var.set(color)

def parse_html():
    text.tag_remove("tag", '1.0', tk.END)
    text.tag_remove("attribute", '1.0', tk.END)
    text.tag_remove("highlight", '1.0', tk.END)

    html_code = text.get('1.0', tk.END)
    soup = BeautifulSoup(html_code, 'html.parser')
    lexer = HtmlLexer()
    style = get_style_by_name('default')

    for token, value in lex(html_code, lexer):
        if token in lexer.tokens:
            start = text.search(value, '1.0', tk.END)
            while start:
                end = text.index(f"{start}+{len(value)}c")
                text.tag_add("highlight", start, end)
                start = text.search(value, end, tk.END)
        elif token == lexer.attributes:
            start = text.search(value, '1.0', tk.END)
            while start:
                end = text.index(f"{start}+{len(value.split('=')[0])}c")
                text.tag_add("attribute", start, end)
                start = text.search(value, end, tk.END)

window = tk.Tk()
window.title("HTML Editor")

# Create the scrolled text area
text = scrolledtext.ScrolledText(window, wrap=tk.WORD)
text.pack(fill=tk.BOTH, expand=True)

# Create the menu bar
menu_bar = tk.Menu(window)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=False)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Close", command=close_app)

# Add the File menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Create the Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=False)

# Add the Edit menu to the menu bar
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Create the View menu
view_menu = tk.Menu(menu_bar, tearoff=False)
view_menu.add_command(label="Preview", command=preview)

# Add the View menu to the menu bar
menu_bar.add_cascade(label="View", menu=view_menu)

# Configure the window to use the menu bar
window.config(menu=menu_bar)

# Create the HTML tag dropdown menu
tag_var = tk.StringVar()
tag_menu = tk.OptionMenu(window, tag_var, *["", "h1", "h2", "h3", "p", "div"])
tag_menu.pack(side=tk.LEFT, padx=5)

# Create the color picker button
color_var = tk.StringVar()
color_var.set("#000000")  # Default color is black
color_button = tk.Button(window, text="Pick Color", command=choose_color)
color_button.pack(side=tk.LEFT, padx=5)

# Create the insert button
insert_button = tk.Button(window, text="Insert Tag", command=insert_tag)
insert_button.pack(side=tk.LEFT, padx=5)

# Bind the parse_html function to text changes
text.bind('<<Modified>>', lambda e: parse_html())

# Parse HTML and apply initial highlighting
parse_html()

# Start the main loop
window.mainloop()
