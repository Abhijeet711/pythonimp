#write a program to count the number of characters in string.
#sample string: google.com
#expected result: ('o':3,'g':2,'.':1,'e':1,'l':1,'m':1,'c':1)
q="y"
while q.lower()=="y":
    a=input("input string: ")
    k=""
    s=[]
    f=[]
    for i in a:
        s.append(i)
        #print(i,end="")
        k=(i,s.count(i))
        f.append(k)
    print(tuple(f))
    q=input("want to continue?(y/n):")
