#write a program using function that returns TRUE if each type in input list
#is atleast as big as the one before it.

def ascending(lst):
    j=0
    for i in range(1, len(lst)):
        if not(lst[j]<=lst[i]):
            return False
        j+=1
    return True

while(True):
    lst=[]
    n=int(input("Enter number of elements in list: "))
    for i in range(n):
        lst.append(input("Enter your element: "))
    if ascending(lst):
        print("List is ascending")
    else:
        print("List is not ascending")
    
    
