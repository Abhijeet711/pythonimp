def ascending_check(lst):
    j = 0
    for i in range(1, len(lst)):
        if not (lst[j]<=lst[i]):
            return False
        j+=1
    return True

while (True):
    lst=[]
    n=int(input("enter how many number of elements you want in the list: "))
    for i in range(n):
        lst.append(int(input("Enter your element: ")))
    if ascending_check(lst):
        print("List is ascending")
    else:
        print("List is not in ascending order")
