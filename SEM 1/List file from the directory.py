import os
q="y"
while q.lower()=="y":
    str1=input("Enter Path:")
    print(os.listdir(str1))
    q=input("Want to continue? (y/n): ")
    
    
