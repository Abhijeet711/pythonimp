q='y'
while q.lower()=='y':
    str1=input('Enter String: ')
    if len(str1)<2:
        str2=str1+str1
    else:
        str2=str1[0:2]+str1[-2:]
    print(str2)
    q=input("want to continue? y/n: ") 
