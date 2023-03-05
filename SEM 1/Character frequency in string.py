b='y'
while b.lower()=='y':
    a=input("input string: ")
    k=""
    s=[]
    f=[]
    for i in a:
        s.append(i)
        k=(i,s.count(i))
        f.append(k)
    print(tuple(f))
    b=input("do you want to continue(y/n)?:")

