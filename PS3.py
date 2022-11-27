#Write a python program to add 'ing' at the end of the given string(length should be atleat 3.
#If the given string already ends with 'ing' then add 'ly' instead.
#If the length of given string is less than 3, leave it unchanged.
#sample string: "abc"
#expected result: "abcing"
#sample string: "abing"
#expected result: "abingly"
q="y"
while q.lower()=="y":
    string = input("add string: ")
    if len(string) < 3:
      print(string)
    elif string[-3:] == 'ing':
      print(string + 'ly')
    else:
      print(string + 'ing')
    
    q=input("want to continue?(y/n):")
