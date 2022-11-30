#Write a python program to create to dictionary with key a first character and value as words starting with that character.
#The program takes a string and creates a dictionary with key as first character and value as words starting with that character.

#Example:
#Enter String: Python is my most favorite programming language in the entire world
#(‘e’,’:’,[‘entire’])
#(‘f’,’:’,[‘favourite’])
#(‘i’,’:’,[‘is’,’in’])
#(‘m’,’:’,[‘most’,’my’])
#(‘l’,’:’,[‘language’])
#(‘p’,’:’,[‘Programming’,’python’])
#(‘t’,’:’,[‘the’])
#(‘w’,’:’[‘world’])
q="y"
while q.lower()=="y":
    dic={}
    all_keys=dic.keys()
    str=input("Enter Your String:")
    str_copy=str.lower()
    lst=str_copy.split()
    lst.sort()
    for i in lst:
        if i[0] in all_keys:
            dic[i[0]].append(i)
        else:
            add=[]
            add.append(i)
            dic[i[0]]=add
    print("Output:",dic)
    q=input("want to continue?(y/n):")
