import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
window = tk.Tk()
window.title("Login System")
image = Image.open('C:\\Users\\admin\\Documents\\GitHub\\Demate-PLDL01E\\Activity6\\LPU.jpg')
bck_pic = ImageTk.PhotoImage(image.resize((1920, 1080)))
lbl = Label(window, image=bck_pic)
lbl.place(x=1, y=1)

frame=Frame(window, width=600, height=300, bg='maroon').place(x=50, y=200)

heading = Label(frame, text='Sign In', fg='navy blue', bg='white', font=('Calibre', 21, 'bold'))
heading.place(x=50, y=200)

#user section
username=Entry(frame, width=18, fg='black', border=2, bg='white', font=('Calibre', 21, 'bold'))
username.place(x=50, y=250)
username.insert(0, 'Username')
Frame(frame, width=210, height=2, bg='black').place(x=50, y=250)

#password section
password=Entry(frame, width=18, fg='black', border=2, bg='white', font=('Calibre', 21, 'bold'))
password.place(x=50, y=300)
password.insert(0, 'Password')
Frame(frame, width=210, height=2, bg='black').place(x=50, y=300)

#button section

window.mainloop()