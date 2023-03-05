q="y"
while q.lower()=="y":
    listing=input("Enter character separated by space:")
    list1=listing.split()
    a=input("Enter a number: ")
    n=int(a)
    list2=[]
    for i in range(1, n+1):
        for j in list1:
            list2.append(str(j)+str(i))
    print(list2)
    q=input("want to continue?(y/n)?:")
