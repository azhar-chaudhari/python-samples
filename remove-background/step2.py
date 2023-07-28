import cv2
import numpy as np
from tkinter import Tk, Button, Label
from tkinter.filedialog import askopenfilename
from matplotlib import pyplot as plt

def browse_image():
    Tk().withdraw()  # Hide the Tkinter root window
    filename = askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])  # Show the file dialog
    if filename:
        remove_background(filename)

def remove_background(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to create a binary image
    _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the binary image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask of the same size as the image
    mask = np.zeros_like(image)

    # Draw the contours on the mask
    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    # Apply the mask to the image
    result = cv2.bitwise_and(image, mask)

    # Display the original image and the result
    plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(122), plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB)), plt.title('Background Removed')
    plt.show()

# Create the GUI window
window = Tk()

# Create the browse image button
browse_button = Button(window, text="Browse Image", command=browse_image)
browse_button.pack()

# Create the remove background button
#remove_button = Button(window, text="Remove Background", command=lambda: remove_background(image_path))
#remove_button.pack()

# Run the GUI event loop
window.mainloop()
