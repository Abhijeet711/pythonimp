ch='y'
while ch.lower()=='y':
    import re
    def display():
        print("Multiplicative Cipher")
        print("MENU:\nEnter 'E' for Encryption \nEnter 'D' for DECRYPTION \nEnter 'X' for Exit \n")
        choice()
    def choice():
        while True:
            ch=(input("Please enter your choice:"))
            if ch not in('E','D','X'):
                print("Not an appropriate choice!")
            else:
                break
        if ch=='E':
            print("Welcome to Encryption")
            encryption()
        elif ch=='D':
            print("Welcome to Decryption")
            decryption()
        elif ch=='X':
            print("The Program is now terminated!")
        else:
            choice()

    print()

    def plain_text():
        while True:
            plaintext=input("Enter plain text:").strip()
            if plaintext.isalpha() or bool(re.search(r"\s",plaintext)):
                return plaintext.upper()
            else:
                print("Enter a Valid text!")

    def cipher_text():
        while True:
            ciphertext=input("Enter cipher text:").strip()
            if ciphertext.isalpha() or bool(re.search(r"\s",ciphertext)):
                return ciphertext.upper()
            else:
                print("Enter a valid text")

    def key():
        while True:
            in_key=input("Enter the key:")
            if in_key.isdecimal():
                return in_key
            else:
                print("Invalid key entered!")

    def encryption():
        ct=""
        pt=plain_text()
        k=int(key())
        try:
            for i in pt.split():
                for j in i:
                    total=(((ord(j)-65)*k)%26)
                    ct=ct+(chr(total+65))
                ct=ct+" "
            print("Cipher Text is:",ct.lower())
        except:
            print("Something went Wrong")
            encryption()
        display()

    def inverse():
        a=int(key())
        a=a%26
        for x in range(1,26):
            if(a*x)%26==1:
                return x
        return 1

    def decryption():
        plt = ""
        ct = cipher_text()
        k = inverse()
        try:
            if True:
                for i in ct.split():
                    for j in i:
                        total = (((ord(j) - 65) * k) % 26)
                        plt = plt + (chr(total + 65))
                    plt = plt + " "
                print("Plain Text is: ", plt.upper())
        except:
            print("Something went wrong")
            decryption()
        display()
    display()
    ch=input("Want to continue(y/n)?: ")
