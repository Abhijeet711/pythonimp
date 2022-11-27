#write a program to get a string made of first two charactes and last 2 characters
#from a given string. If the string is less than 2, return instead of an empty string.
#sample string: "python programming"
#expected result: "pyng"
#sample string: "py"
#expected result: "pypy"
q="y"
while q.lower()=="y":
    u1=input('enter string:')
    if len(u1)<2:
        print(u1*2)
    elif len(u1)>2:
        print(u1[0:2]+u1[-2:])
    q=input("want to continue?(y/n):")
