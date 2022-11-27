#write a python program having function rotatelist that takes list l and
#a positive integerk and return the list k after k number of rotations.
#if k is not positive, return list l unchanged.

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

inputList()
print("list before rotation: ",l)
k=int(input("enter number of rotation:"))
rotateList(l,k)
print("list after rotation: ", l)
