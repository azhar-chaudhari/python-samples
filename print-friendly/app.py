import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import urllib.request

def submit_url():
    url = url_entry.get()

    try:
        # Load the URL content
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')

        # Clear the text area
        text_area.delete('1.0', tk.END)

        # Display the print-friendly page
        text_area.insert(tk.END, html)
    except urllib.error.URLError:
        text_area.delete('1.0', tk.END)
        error_message = f'Error: {str(e)}\n\n{traceback.format_exc()}'
        text_area.insert(tk.END, error_message)

root = tk.Tk()
root.title("Print-Friendly Page")

# URL Entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_url)
submit_button.pack()

# Scrollable Text Area
text_area = scrolledtext.ScrolledText(root, height=10)
text_area.pack()

root.mainloop()
