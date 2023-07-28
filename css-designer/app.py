import tkinter as tk

def generate_css():
    css_code = ".my-element {"

    # Border Styles
    if border_width.get():
        css_code += f"\n    border-width: {border_width.get()}px;"
    if border_style.get():
        css_code += f"\n    border-style: {border_style.get()};"
    if border_color.get():
        css_code += f"\n    border-color: {border_color.get()};"
    if border_radius.get():
        css_code += f"\n    border-radius: {border_radius.get()}px;"

    # Paddings and Margins
    if padding.get():
        css_code += f"\n    padding: {padding.get()}px;"
    if margin.get():
        css_code += f"\n    margin: {margin.get()}px;"

    # Text Styles
    if text_color.get():
        css_code += f"\n    color: {text_color.get()};"
    if font_family.get():
        css_code += f"\n    font-family: {font_family.get()};"
    if font_size.get():
        css_code += f"\n    font-size: {font_size.get()}px;"
    if font_weight.get():
        css_code += f"\n    font-weight: {font_weight.get()};"
    if text_align.get():
        css_code += f"\n    text-align: {text_align.get()};"
    if text_decoration.get():
        css_code += f"\n    text-decoration: {text_decoration.get()};"

    # Background Styles
    if background_color.get():
        css_code += f"\n    background-color: {background_color.get()};"
    if background_image.get():
        css_code += f'\n    background-image: url("{background_image.get()}");'
    if background_repeat.get():
        css_code += f"\n    background-repeat: {background_repeat.get()};"
    if background_position.get():
        css_code += f"\n    background-position: {background_position.get()};"

    # Position Styles
    if position.get():
        css_code += f"\n    position: {position.get()};"
    if top.get():
        css_code += f"\n    top: {top.get()}px;"
    if right.get():
        css_code += f"\n    right: {right.get()}px;"
    if bottom.get():
        css_code += f"\n    bottom: {bottom.get()}px;"
    if left.get():
        css_code += f"\n    left: {left.get()}px;"
    if z_index.get():
        css_code += f"\n    z-index: {z_index.get()};"

    css_code += "\n}"
    
    css_output.delete(1.0, tk.END)
    css_output.insert(tk.END, css_code)


# Create the main application window
root = tk.Tk()
root.title("CSS Template Designer")

# Create variables to store user input
border_width = tk.IntVar(value=1)
border_style = tk.StringVar(value="solid")
border_color = tk.StringVar(value="#000000")
border_radius = tk.IntVar(value=0)
padding = tk.IntVar(value=0)
margin = tk.IntVar(value=0)
text_color = tk.StringVar(value="#000000")
font_family = tk.StringVar(value="Arial")
font_size = tk.IntVar(value=12)
font_weight = tk.StringVar(value="normal")
text_align = tk.StringVar(value="left")
text_decoration = tk.StringVar(value="none")
background_color = tk.StringVar(value="#ffffff")
background_image = tk.StringVar(value="")
background_repeat = tk.StringVar(value="no-repeat")
background_position = tk.StringVar(value="left top")
position = tk.StringVar(value="static")
top = tk.IntVar(value=0)
right = tk.IntVar(value=0)
bottom = tk.IntVar(value=0)
left = tk.IntVar(value=0)
z_index = tk.IntVar(value=0)

# Create input labels and entry fields for each property
border_width_label = tk.Label(root, text="Border Width:")
border_width_label.pack()
border_width_entry = tk.Entry(root, textvariable=border_width)
border_width_entry.pack()

border_style_label = tk.Label(root, text="Border Style:")
border_style_label.pack()
border_style_entry = tk.Entry(root, textvariable=border_style)
border_style_entry.pack()

border_color_label = tk.Label(root, text="Border Color:")
border_color_label.pack()
border_color_entry = tk.Entry(root, textvariable=border_color)
border_color_entry.pack()

border_radius_label = tk.Label(root, text="Border Radius:")
border_radius_label.pack()
border_radius_entry = tk.Entry(root, textvariable=border_radius)
border_radius_entry.pack()

padding_label = tk.Label(root, text="Padding:")
padding_label.pack()
padding_entry = tk.Entry(root, textvariable=padding)
padding_entry.pack()

margin_label = tk.Label(root, text="Margin:")
margin_label.pack()
margin_entry = tk.Entry(root, textvariable=margin)
margin_entry.pack()

text_color_label = tk.Label(root, text="Text Color:")
text_color_label.pack()
text_color_entry = tk.Entry(root, textvariable=text_color)
text_color_entry.pack()

font_family_label = tk.Label(root, text="Font Family:")
font_family_label.pack()
font_family_entry = tk.Entry(root, textvariable=font_family)
font_family_entry.pack()

font_size_label = tk.Label(root, text="Font Size:")
font_size_label.pack()
font_size_entry = tk.Entry(root, textvariable=font_size)
font_size_entry.pack()

font_weight_label = tk.Label(root, text="Font Weight:")
font_weight_label.pack()
font_weight_entry = tk.Entry(root, textvariable=font_weight)
font_weight_entry.pack()

text_align_label = tk.Label(root, text="Text Align:")
text_align_label.pack()
text_align_entry = tk.Entry(root, textvariable=text_align)
text_align_entry.pack()

text_decoration_label = tk.Label(root, text="Text Decoration:")
text_decoration_label.pack()
text_decoration_entry = tk.Entry(root, textvariable=text_decoration)
text_decoration_entry.pack()

background_color_label = tk.Label(root, text="Background Color:")
background_color_label.pack()
background_color_entry = tk.Entry(root, textvariable=background_color)
background_color_entry.pack()

background_image_label = tk.Label(root, text="Background Image:")
background_image_label.pack()
background_image_entry = tk.Entry(root, textvariable=background_image)
background_image_entry.pack()

background_repeat_label = tk.Label(root, text="Background Repeat:")
background_repeat_label.pack()
background_repeat_entry = tk.Entry(root, textvariable=background_repeat)
background_repeat_entry.pack()

background_position_label = tk.Label(root, text="Background Position:")
background_position_label.pack()
background_position_entry = tk.Entry(root, textvariable=background_position)
background_position_entry.pack()

position_label = tk.Label(root, text="Position:")
position_label.pack()
position_entry = tk.Entry(root, textvariable=position)
position_entry.pack()

top_label = tk.Label(root, text="Top:")
top_label.pack()
top_entry = tk.Entry(root, textvariable=top)
top_entry.pack()

right_label = tk.Label(root, text="Right:")
right_label.pack()
right_entry = tk.Entry(root, textvariable=right)
right_entry.pack()

bottom_label = tk.Label(root, text="Bottom:")
bottom_label.pack()
bottom_entry = tk.Entry(root, textvariable=bottom)
bottom_entry.pack()

left_label = tk.Label(root, text="Left:")
left_label.pack()
left_entry = tk.Entry(root, textvariable=left)
left_entry.pack()

z_index_label = tk.Label(root, text="Z-Index:")
z_index_label.pack()
z_index_entry = tk.Entry(root, textvariable=z_index)
z_index_entry.pack()

generate_button = tk.Button(root, text="Generate CSS", command=generate_css)
generate_button.pack()

# Create a text area to display the generated CSS code
css_output = tk.Text(root, height=10, width=50)
css_output.pack()

root.mainloop()
