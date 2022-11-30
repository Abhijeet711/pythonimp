#write a program to display all files under specific directory.
import os
q="y"
while q.lower()=="y":
    os.system("CLS")
    str = input("Enter Your Path:")
    print(os.listdir(str))
    q=input("want to continue?(y/n):")
