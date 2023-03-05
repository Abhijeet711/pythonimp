q="y"
while q.lower()=="y":
    dic={}
    all_keys=dic.keys()
    str=input("Enter your string: ")
    str_copy = str.lower()
    lst=str_copy.split()
    lst.sort()
    for i in lst:
        if i[0] in all_keys:
            dic[i[0]].append(i)
        else:
            add=[]
            add.append(i)
            dic[i[0]]=add
    print("Output: ",dic)
    q=input("want to continue? (y/n):")
