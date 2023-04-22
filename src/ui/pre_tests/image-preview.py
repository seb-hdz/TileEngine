from PIL import ImageTk, Image
import tkinter as tk


class ImagePreview:
    def __init__(self, image_path):
        # Load the image using Pillow
        image = Image.open(image_path)

        # Create a Tkinter window and canvas
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=image.width, height=image.height)
        self.canvas.pack()

        # Convert the image to a Tkinter-compatible format and display it
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Run the Tkinter event loop
        self.root.mainloop()


if __name__ == "__main__":
    preview = ImagePreview("")
