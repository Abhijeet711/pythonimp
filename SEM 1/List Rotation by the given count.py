def rotatevalue(l):
    lastvalue=l[-1]
    for i in reversed(range(len(l)-1)):
        l[i+1]=l[i]
    l[0]=lastvalue
    
def rotateList(l, k):
    for numb in range(k):
        rotatevalue(l)

l=[]
def inputList():
    user = int(input("Number of items in list: "))
    for j in range(user):
        w=int(input("Enter items in list: "))
        l.append(w)

q="y"
while q.lower()=="y":
    inputList()
    print("list before rotation: ",l)
    k=int(input("enter number of rotation:"))
    rotateList(l,k)
    print("list after rotation: ", l)
    q=input("want to continue?(y/n): ")
