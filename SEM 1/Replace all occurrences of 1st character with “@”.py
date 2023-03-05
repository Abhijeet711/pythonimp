ch='y'
while ch.lower()=='y':
    str1=input("Enter a string:")
    a=str1.lower()
    char=input("Enter a character from which to replace:")
    frst=a[0]
    str2=a[1:].replace(frst,char)
    print(" Expected Result: ",str1[:1]+str2)
    ch=input("Want to continue(y/n)?:")
