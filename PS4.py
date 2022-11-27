#Write a python program to get a string from a given string where all occurances
# of its first character have been changed to "@" except the first character itself.
#sample string: "restart"
#expected result: "resta@t"
q="y"
while q.lower()=="y":
    str1=input("Enter a string: ")
    a=str1.lower()
    char=input("Enter a character fron which to replace: ")
    frst=a[0]
    str2=a[1:].replace(frst,char)
    print("Result: ", str1[:1]+str2)
    q=input("Want to continue?(y/n): ")
