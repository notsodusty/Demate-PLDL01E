import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
#window
window = tk.Tk()
window.title("Assessment Form")
window.geometry('1520x900')
image = Image.open("C:\\Users\\admin\\Pictures\\Screenshots\\Screenshot.png")


class design_gui_inteface():
    def __int__(self, frame1):
        frame1 = ''
    def frames(self, x, y):
        self.frame1 = Frame(window, width=1100, height=160, border=0, bg='light gray')
        self.frame1.place(x=x, y=y)
    def heading_design(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', font=('Algerian', 30, 'bold'))
        self.heading.place(x=x, y=y)
    def textbox_design1(self, x, y):
        self.textbox = Text(width=25, height= 1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)
    def textbox_design2(self, x, y):
        self.textbox = Text(width=31, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)
    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='light gray', font=('Calibre', 10))
        self.lbl.place(x=x, y=y)
    def button_design(self, x, y, text_value, width_value, bg_value):
        self.bg_value = bg_value
        self.width_value = width_value
        self.text_value = text_value
        self.upload_button = Button(width=width_value, pady=7, text=text_value, bg=bg_value,
                            fg='white', cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)
    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width