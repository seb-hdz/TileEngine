import tkinter as tk
from PIL import ImageTk


class ImagePreview(tk.LabelFrame):
    def __init__(self, master, image_data):
        super().__init__(master, text="Image Preview")

        # Create canvas
        self.canvas = tk.Canvas(self, width=512, height=512)
        self.canvas.pack()

        # Load the image using Pillow
        self.image = ImageTk.PhotoImage(image_data)

        # Display the image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

    def update_image(self, image_data):
        # Update the image
        new_image = ImageTk.PhotoImage(image_data)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=new_image)
