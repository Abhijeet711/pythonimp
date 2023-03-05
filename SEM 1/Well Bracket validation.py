q='y'
while q.lower()=='y':
    def wellbracketed(str):
        if str.count('(')==str.count(')') and str.count('[')== str.count(']') and str.count('{')== str.count('}'):
            return True
        else:
            return False
    str=input("Enter your string: ")
    if wellbracketed(str):
        print("String is well bracketed")
    else:
        print("String is not well bracketed")
    q=input("Want to continue?(y/n): ")
