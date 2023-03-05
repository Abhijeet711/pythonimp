import tkinter
from tkinter import *

root = tkinter.Tk(className="checkBox")

root.geometry("500x135")

l1=Label(root, text='Select your preferred programming language:',font="times 15")
l1.place(x=10,y=10)

language1 = IntVar()
language2 = IntVar()
language3 = IntVar()
c1=Checkbutton(root, text='JAVA', variable=language1, onvalue=1, offvalue=0, font="times 15", bg="pink",activebackground= "#4a330d", activeforeground="#f1ddbe")
c1.place(x=385,y=10)
c2=Checkbutton(root, text='Python', variable=language2, onvalue=1, offvalue=0, font="times 15", bg="pink",activebackground= "#4a330d", activeforeground="#f1ddbe")
c2.place(x=385,y=50)
c3=Checkbutton(root, text='C', variable=language3, onvalue=1, offvalue=0, font="times 15", bg="pink",activebackground= "#4a330d", activeforeground="#f1ddbe")
c3.place(x=385,y=90)    

root.mainloop()