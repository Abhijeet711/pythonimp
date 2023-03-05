import re
q = 'y'
while q.lower() == 'y':
    password = input("\nEnter the Password: ")
    length = len(password)
    if length >= 6:
        if length <= 16:
            if(re.findall(r'[a-zA-Z]',password)):
                if(re.findall(r'\d',password)):
                    if(re.findall(r'[$#@]',password)):
                        print("Password is valid")
                    else:
                        print("password should have [$#@]")
                else:
                    print("password should have one digit")
            else:
                print("password should have one alphabet")
        else:
            print("length of password should be less than 16")
    else:
        print("length of password should be atleast 6")
    q=input("want to continue? (y/n): ")
