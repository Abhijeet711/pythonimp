class power:
    def __init__(self,x):
        self.x=x
    def pow(self,n):
        return self.x**n

q="y"
while q.lower()=="y":
    a=int(input("a: "))
    p=power(a)
    b=int(input("b: "))
    print(p.pow(b))
    q=input("want to continue?(y/n): ")
