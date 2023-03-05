class twosum:
  def findindexes(self,lst,target):
    lol=len(lst)
    print("Pairs whose sum is ",target)
    for i in range(lol):
      for j in range(i,lol):
        if(lst[i]+lst[j]==target):
          print(lst[i],lst[j],end=",")

q="y"
while q.lower()=="y":
  n=int(input("Enter number of elements: "))
  lst=[]
  for i in range(n):
    ele=int(input("Enter element: "))
    lst.append(ele)
  print(lst)
  target=int(input("Enter a target of sum of two indexes: "))
  t=twosum()
  print(t.findindexes(lst,target))
  q=input("want to continue?(y/n):")
