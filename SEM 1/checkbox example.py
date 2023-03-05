import tkinter
from tkinter import *

# where root is the name of the main window object. To change the name of window we've to give className="", it will always be in camel case.
root = tkinter.Tk(className="checkBox")

# geometry("widthxheight") sets the size of the window.
root.geometry("250x85")

# Check Box Example:
l1=Label(root, text='Select courses you\'ve done:')
l1.place(x=10,y=10)

# creating variables to be used in the Checkbox
course1 = IntVar()
course2 = IntVar()
course3 = IntVar()
c1=Checkbutton(root, text='MCA', variable=course1, onvalue=1, offvalue=0)
c1.place(x=165,y=10)
c2=Checkbutton(root, text='MBA', variable=course2, onvalue=1, offvalue=0)
c2.place(x=165,y=30)
c3=Checkbutton(root, text='M.Tech', variable=course3, onvalue=1, offvalue=0)
c3.place(x=165,y=50)    

#mainloop() is used when your application is ready to run. mainloop() is an infinite loop used to run the application.
root.mainloop()