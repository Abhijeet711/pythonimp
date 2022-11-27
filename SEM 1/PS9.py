#write a python program to check if the given string is well bracketed or not.

q="y"
while q.lower()=="y":
    def wellbracketed(str):
        if str.count('(') == str.count(')'):
            return True
        else:
            return False
        if str.count('{') == str.count('}'):
            return True
        else:
            return False
        if str.count('[') == str.count(']'):
            return True
        else:
            return False
    str=input("Enter Your String:")
    if wellbracketed(str):
        print("String is well bracketed.")
    else:
        print("String is not well bracketed.")
    q=input("want to continue?(y/n): ")

