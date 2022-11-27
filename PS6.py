#Write a python program to convert a list of multiple integer into simple integer
#Sample String: [11,30,40]
#expected result: 113040


number_list=[]
n=int(input("Enter List Size:"))
for i in range(0,n):
    print("Enter number at index",i,)
    item=int(input())
    number_list.append(item)
print("List is: ", number_list)
print("List to simple integer: ")
for i in number_list:
    print(i,end="")
