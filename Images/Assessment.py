import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Assessment Form")
image = Image.open('C:\\Users\\admin\\Documents\\GitHub\\Demate-PLDL01E\\Activity6\\LPU.jpg')
bck_pic = ImageTk.PhotoImage(image.resize((1920, 1080)))
lbl = Label(window, image=bck_pic)
lbl.place(x=1, y=1)

class Design_GUI_Interface():
    def __int__(self, frame1, frame2, frame3):
        frame1= ''
    def frames(self, x, y):
        self.frame1 = Frame(window, width=1050, height=170, border=0, bg='#9c2824')
        self.frame1.place(x=x, y=y)

    def frames2(self, x, y):
        self.frame2 = Frame(window, width= 1050, height=120, border=0, bg='#9c2824')
        self.frame2.place(x=x, y=y)

    def frames3(self, x, y):
        self.frame3 = Frame(window, width= 1050, height=300, border=0, bg='#9c2824')
        self.frame3.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=25, height= 1, fg='black', bg='white',
 font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)
    def textbox_design2(self, x, y):
        self.textbox = Text(width=28, height=1, fg='black', bg='white',
 font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)
    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='#9c2824', fg='white', font=('Times New Roman', 11, 'bold'))
        self.lbl.place(x=x, y=y)

my_gui_design = Design_GUI_Interface()
#call frames attribute within the class named as design_gui_interface
#call for frame 1
my_gui_design.frames(100, 220)
#call for frame 2
my_gui_design.frames2(100, 400)
#call for frame 3
my_gui_design.frames3(100, 600)


studentnametxt = my_gui_design.textbox_design1(150, 260)
studentcoursetxt = my_gui_design.textbox_design1(x=400, y=260)
studentnumbertxt = my_gui_design.textbox_design1(x=650, y=260)
academicyeartxt = my_gui_design.textbox_design1(900, 260)
currentdatetxt = my_gui_design.textbox_design1(150, 330)

departmenttxt = my_gui_design.textbox_design2(150, 450)
designationtxt = my_gui_design.textbox_design2(450, 450)
employee_statustxt = my_gui_design.textbox_design2(750, 450)


lpufeetxt = my_gui_design.textbox_design2(150, 650)
athleticfeetxt = my_gui_design.textbox_design2(400, 650)
audiovisualfeetxt = my_gui_design.textbox_design2(650, 650)
ausgfeetxt = my_gui_design.textbox_design2(900, 650)
culturalfeetxt = my_gui_design.textbox_design2(150, 700)
energycosttxt = my_gui_design.textbox_design2(400, 700)
guidancetxt = my_gui_design.textbox_design2(650, 700)
insurancetxt = my_gui_design.textbox_design2(900, 700)
learningsystemfeetxt = my_gui_design.textbox_design2(150, 750)
libraryfeetxt = my_gui_design.textbox_design2(400, 750)
registrationfeetxt = my_gui_design.textbox_design2(650, 750)
rsofeetxt = my_gui_design.textbox_design2(900, 750)
activityfeetxt = my_gui_design.textbox_design2(150, 800)
technologyfeetxt = my_gui_design.textbox_design2(400, 800)
testpapersfeetxt = my_gui_design.textbox_design2(650, 800)
downpaymenttxt = my_gui_design.textbox_design2(900, 800)


#textbox label for first frame
firstname_lbl = my_gui_design.label_design(150, 235, 'Student Name')
middle_namelbl = my_gui_design.label_design(400, 235, 'Student Course')
surnamelbl = my_gui_design.label_design(650, 235, 'Student ID Number')
suffixlbl = my_gui_design.label_design(900, 235, 'Academic Year')
date_of_birthlbl = my_gui_design.label_design(150, 305, 'Current Date')

#textbox label for second frame
sectionlbl = my_gui_design.label_design(150, 425, 'Section')
subjectslbl = my_gui_design.label_design(450, 425, 'Number of Subjects')
unitslbl = my_gui_design.label_design(750, 425, 'Number of Units')

#textboxlabel for third frame
lpufeelbl = my_gui_design.label_design(150, 625, 'LPU Fee')
athleticfeelbl = my_gui_design.label_design(400, 625, 'Athletic Fee')
audiovisuallbl =  my_gui_design.label_design(650, 625, 'Audio Visual Library Fee')
ausgfeelbl = my_gui_design.label_design(900, 625, 'AUSG Fee')
culturalfeelbl = my_gui_design.label_design(150, 675, 'Cultural Fee')
energycostlbl = my_gui_design.label_design(400, 675, 'Energy Cost, AirCon Fee')
guidancefeelbl = my_gui_design.label_design(650, 675, 'Guidance Fee')
insurancefeelbl = my_gui_design.label_design(900, 675, 'Insurance Fee')
learningsystemfeelbl = my_gui_design.label_design(150, 725, 'Learning System Fee')
libraryfeelbl = my_gui_design.label_design(400, 725, 'Library Fee')
registrationfeelbl = my_gui_design.label_design(650, 725, 'Registration Fee')
rsofeelbl = my_gui_design.label_design(900, 725, 'RSO Fee')
activityfeelbl = my_gui_design.label_design(150, 775, 'Activity Fee')
technologyfeelbl = my_gui_design.label_design(400, 775, 'Technology Fee')
testpapersfeelbl = my_gui_design.label_design(650, 775, 'Test Papers Fee')
downpaymentlbl = my_gui_design.label_design(900, 775, 'Down Payment Fee')


window.mainloop()