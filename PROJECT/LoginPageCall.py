from tkinter import Tk
from LoginPageClass import DesignGUI

# Initialize the main window and the DesignGUI instance
windows = Tk()
app = DesignGUI(windows)

# Create a class that will display the design
class DisplayGUI:
    def background_image(self):
        # Load and display background image
        app.add_image(x=1, y=1, image_path='C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\AV Log-in Page.png', width=1490, height=900)

    def logo(self):
        # Load and display logo in the middle top
        app.add_image(x=648, y=195, image_path='C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\AV Logo.png', width=200, height=120, bg_color='#F9EDED')

    def inner_outerframe(self):
        # Outer frame (acts as the border)
        outer_frame = app.frame(x=530, y=380, w=414, h=227, bg_color='#7A0E0E')

        # Inner frame (centered inside outer frame)
        inner_frame = app.frame(x=533, y=383, w=408, h=221, bg_color='#F9EDED')

    def login_information(self):
        # Heading Label
        app.label(text='Welcome Back', x=620, y=323, font=('Century Gothic', 24, 'bold'))

        # E-mail Address Label Section
        app.label(text='E-mail Address/Username/Phone No.', x=550, y=392, font=('Century Gothic', 11), fg_color='#7A0E0E')
        app.email_textbox = app.entry(x=550, y=427)

        # Password Label Section
        app.label(text='Password', x=550, y=465, font=('Century Gothic', 11), fg_color='#7A0E0E')
        app.password_textbox = app.entry(x=550, y=500, show='*')

        # "Forgot Password?" Label
        app.label(text='Forgot Password?', x=549, y=530, font=('Century Gothic', 8, 'underline'), cursor='hand2', fg_color='#7A0E0E')

    def buttons(self):
        # Buttons
        app.label(text="Don't have an account?", x=570, y=570, font=('Century Gothic', 9, 'bold'), fg_color='#7A0E0E')
        app.label(text="Sign-up", x=845, y=570, font=('Century Gothic', 9, 'bold'), cursor='hand2', fg_color='#7A0E0E')

        # LOGIN Button
        app.button(text='LOGIN', x=695, y=620, bg='#7A0E0E', fg='white', font=('Century Gothic', 12, 'bold'))

# Create an instance of DisplayGUI
login_gui = DisplayGUI()

# Call the functions from DisplayGUI instance
login_gui.background_image()
login_gui.logo()
login_gui.inner_outerframe()
login_gui.login_information()
login_gui.buttons()

# Runs the code
windows.mainloop()