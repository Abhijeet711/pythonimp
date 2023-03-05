b='y'
while b.lower()=='y':
    string=input("add string: ")
    if len(string)<3:
        print(string)
    elif string[-3:]=='ing':
        print(string+'ly')
    else:
        print(string+'ing')
    b=input("do you want to continue(y/n)?:")
