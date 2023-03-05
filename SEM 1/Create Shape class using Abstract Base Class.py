from abc import ABC, abstractmethod
ch="y"
while ch.lower()=="y":
    class shape(ABC):
        @abstractmethod
        def area(self):
            raise NotImplentedError()
        def perimeter(self):
            raise NotImplentedError()
        def display(self):
            raise NotImplentedError()

    class rectangle(shape):
        def __init__(self,l,b):
            self.l = l
            self.br = b
            self.a = 0
            self.b = 0
        def area(self):
            self.a = self.l*self.br
        def perimeter(self):
            self.b = 2*(self.l+self.br)
        def display(self):
            print("Area of rectangle: ",self.a)
            print("Perimeter of rectangle: ",self.b)

    class triangle(shape):
        def __init__(self,base,height,side1,side2):
            self.base = base
            self.height = height
            self.side1 = side1
            self.side2 = side2
            self.a = 0
            self.b = 0
        def area(self):
            self.a = (self.base*self.height)/2
        def perimeter(self):
            self.b = self.base+self.side1+self.side2
        def display(self):
            print("Area of triangle: ",self.a)
            print("Perimeter of triangle: ",self.b)

    class circle(shape):
        def __init__(self,r):
            self.r = r
            self.a = 0
            self.b = 0
        def area(self):
            self.a = self.r*self.r*3.14
        def perimeter(self):
            self.b = 2*self.r*3.14
        def display(self):
            print("Area of circle: ",self.a)
            print("Perimeter of circle: ",self.b)

    class rhombus(shape):
        def __init__(self,d1,d2,side):
            self.d1 = d1
            self.d2 = d2
            self.side = side
            self.a = 0
            self.b = 0
        def area(self):
            self.a = (self.d1+self.d2)/2
        def perimeter(self):
            self.b = 4*self.side
        def display(self):
            print("Area of rhombus: ",self.a)
            print("Perimeter of rhombus: ",self.b)

    print("1. Area and Perimeter of RECTANGLE")
    print("2. Area and Perimeter of TRIANGLE")
    print("3. Area and Perimeter of CIRCLE")
    print("4. Area and Perimeter of RHOMBUS")

    n=int(input("Enter your choice: "))
    
    if(n==1):
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        rect=rectangle(l,b)
        rect.area()
        rect.perimeter()
        rect.display()
    
    elif(n==2):
        base=int(input("Enter base: "))
        height=int(input("Enter height: "))
        side1=int(input("Enter side 1: "))
        side2=int(input("Enter side 2: "))
        tri=triangle(base,height,side1,side2)
        tri.area()
        tri.perimeter()
        tri.display()
    
    elif(n==3):
        radius=int(input("Enter radius: "))
        cir=circle(radius)
        cir.area()
        cir.perimeter()
        cir.display()
    
    elif(n==4):
        d1=int(input("Enter 1st diagonal: "))
        d2=int(input("Enter 2nd diagonal: "))
        side=int(input("Enter side: "))
        roh=rhombus(d1,d2,side)
        roh.area()
        roh.perimeter()
        roh.display()
    ch=input("want to continue?(y/n): ")
    
