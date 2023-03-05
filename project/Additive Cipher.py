q='y'
while q.lower()=='y':
    def encryptdata(string,shiftkey):
        cipher_text=''
        for char in string:
            if char==' ':
                cipher_text=cipher_text+char
            elif char.isupper():
                cipher_text=cipher_text+chr((ord(char)+shiftkey-65)%26+65)
            else:
                cipher_text=cipher_text+chr((ord(char)+shiftkey-97)%26+97)
        return cipher_text

    print("Additive Cipher ")

    plain_text=input("Plain Text: ")
    key=int(input("Key:"))
    print("Plain text:",plain_text)
    print("Encrypted text:",encryptdata(plain_text,key))

    def decryptdata(text,s):
        s=26-s
        result=""
        for i in range(len(text)):
            char=text[i]
            if(char.isupper()):
                result=result+chr((ord(char)+s-65)%26+65)
            else:
                result=result+chr((ord(char)+s-97)%26+97)
        return result

    cipher_text=input("Enter cipher_text text:")
    key=int(input("Enter the key:"))
    print("Decrypted text:",decryptdata(cipher_text,key))
    q=input("want to continue(y/n)?: ")
