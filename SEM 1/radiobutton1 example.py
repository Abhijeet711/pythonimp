import tkinter
from tkinter import *
root = tkinter.Tk(className="radioButton")

root.geometry("365x175")

l1=Label(root, text='Select your favourite sport:',font="times 15")
l1.place(x=10,y=10)

sport = IntVar()
g1=Radiobutton(root, text='Cricket', variable=sport, value="1", font="times 15", bg="yellow",activebackground= "purple", activeforeground="white")
g1.place(x=235,y=10)
g2=Radiobutton(root, text='Football', variable=sport, value="2", font="times 15", bg="yellow",activebackground= "purple", activeforeground="white")
g2.place(x=235,y=50)
g3=Radiobutton(root, text='Tennis', variable=sport, value="3", font="times 15", bg="yellow",activebackground= "purple", activeforeground="white")
g3.place(x=235,y=90)
g4=Radiobutton(root, text='Volleyball', variable=sport, value="4", font="times 15", bg="yellow",activebackground= "purple", activeforeground="white")
g4.place(x=235,y=130)

root.mainloop()