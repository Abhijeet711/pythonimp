q="y"
while q.lower()=="y":
    print("Using add(+) on Integer:")
    n1 = int(input("Enter the num 1: "))
    n2 = int(input("Enter the num 2: "))
    print("Sum of integers num1 + num2: ",n1+n2)
    print("\nUsing + on String:")
    s1 = input("Enter the str 1: ")
    s2 = input("Enter the str 2: ")
    print("Concatenation of string str1 + str2: ",s1+s2)
    print("\nUsing + on List:")
    l1= []
    no_of_ele = int(input("Enter the no. of elements for the list 1: "))
    for i in range(no_of_ele):
        ele = int(input("Enter the integer element for the list 1 : "))              
        l1.append(ele)
    l2= []
    no_of_ele = int(input("\nEnter the no. of elements for the list 2: "))
    for i in range(no_of_ele):
        ele = int(input("Enter the integer element for the list 2 : "))                
        l2.append(ele)
    print("\nlist 1: ",l1)
    print("list 2: ",l2)
    print("Concatenation of list list1 + list2: ",l1+l2)
    class add:
        def __init__(self, name):
            self.name = name

        def __add__(self,other):
            return self.name + other.name

    class subadd:
        def __init__(self, name):
            self.name = name

    class1_obj = add("type")
    class2_obj = subadd("writer")
    print("Concatenation of Class Object class1_obj + class2_obj: ",class1_obj+class2_obj)
    q=input("want to continue?(y/n): ")
