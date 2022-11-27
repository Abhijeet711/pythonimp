#Write a program to create list by concatenating a given list which range goes
#from 1 to n.
#Sample String: ['p','q']; n=3
#exected result: ['p1','q1','p2','q2','p3','q3']
q="y"
while q.lower()=="y":
    listinp=input("Enter character separated by space: ")
    list1=listinp.split()
    a=input("Enter a number: ")
    n=int(a)
    list2=[]
    for i in range(1,n+1):
        for j in list1:
            list2.append(str(j)+str(i))
    print(list2)
    q=input("want to continue?(y/n):")

