import tkinter
from tkinter import *

# where root is the name of the main window object. To change the name of window we've to give className="", it will always be in camel case.
root = tkinter.Tk(className="radioButton")

# geometry("widthxheight") sets the size of the window.
root.geometry("250x40")

# Radio button example:
l1=Label(root, text='Select your gender:')
l1.place(x=10,y=10)

# creating variable to be used in the Radiobutton
gender = IntVar()
g1=Radiobutton(root, text='Male', variable=gender, value="1")
g1.place(x=115,y=10)
g2=Radiobutton(root, text='Female', variable=gender, value="2")
g2.place(x=170,y=10)

#mainloop() is used when your application is ready to run. mainloop() is an infinite loop used to run the application.
root.mainloop()