#write a program that finds the largest file in the given dictonary.

import os
q="y"
while q.lower()=="y":
    str = input("Enter Your Path:")
    name = ''
    size = -1
    file_lst = os.listdir(str)
    for i in file_lst:
        if os.path.isfile(i):
            tmp_size = os.path.getsize(i)
            if tmp_size > size:
                size = tmp_size
                name = i
    print("Greatest File Is {} with File Size Is {}".format(name, size))
    q=input("want to continue?(y/n):")
