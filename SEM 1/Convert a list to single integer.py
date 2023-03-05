q="y"
while q.lower()=="y":
    number_list=[]
    n=int(input("Enter list size: "))
    for i in range(0,n):
        print("Enter number at index: ", i , )
        item=int(input())
        number_list.append(item)
    print("List is ", number_list)
    print("List to single integer: ")
    for i in number_list:
        print(i,end='')
    q=input("\nwant to continue?(y/n): ")
