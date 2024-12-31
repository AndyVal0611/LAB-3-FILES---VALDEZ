import tkinter as tk
from tkinter import Label, Frame, Text, Button, ttk
from PIL import Image, ImageTk

class DesignGUI:
    def __init__(self, window):
        self.window = window

    def create_frame(self, x, y, width, height, bg='#c4c0c0'):
        frame = Frame(self.window, width=width, height=height, bg=bg)
        frame.place(x=x, y=y)
        return frame

    def create_heading(self, x, y, text):
        heading = Label(self.window, text=text, fg='black', bg='#f6f4f4', font=('Algerian', 25, 'bold'))
        heading.place(x=x, y=y)
        return heading

    def create_label(self, x, y, text, font=('Segoe UI', 9), bg='#c4c0c0'):
        label = Label(self.window, text=text, bg=bg, font=font)
        label.place(x=x, y=y)
        return label

    def create_textbox(self, x, y, width=25, height=1, bg_color='white'):
        textbox = Text(self.window, width=width, height=height, fg="black", bg=bg_color, font=('Segoe UI', 9))
        textbox.place(x=x, y=y)
        return textbox

    def create_combobox(self, x, y, values, width=22):
        combo = ttk.Combobox(self.window, width=width, values=values, font=('Segoe UI', 9))
        combo.place(x=x, y=y)
        return combo

    def create_button(self, x, y, text, width=10, height=1, command=None, font=('Segoe UI', 10), fg='black', bg='blue'):
        button = Button(self.window, text=text, width=width, height=height, bg=bg, fg=fg, font=font, command=command)
        button.place(x=x, y=y)
        return button

    def create_image(self, image_path, x, y, width, height):
        image = Image.open(image_path)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)
        label = Label(self.window, image=photo, bg='white')
        label.image = photo  # Prevent garbage collection
        label.place(x=x, y=y)
        return label