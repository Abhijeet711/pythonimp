import string
import random
ch='y'
while ch.lower()=='y':
    print("Vernam Cipher")
    number_to_alphabet_dict = { 1:'a',2:'b',3:'c',4:'d',5:'e'
                               ,6:'f',7:'g',8:'h',9:'i',10:'j'
                               ,11:'k',12:'l',13:'m',14:'n',15:'o'
                               ,16:'p',17:'q',18:'r',19:'s',20:'t'
                               ,21:'u',22:'v',23:'w',24:'x',25:'y'
                               ,26:'z'}

    alphabet_to_number_dict = {  'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5
                               , 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10
                               , 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15
                               , 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20
                               , 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25
                               , 'z': 26}
    def getMode():
        while True:
            print("Do you want to encrypt or decrypt ")
            mode = str(input()).lower()
            if mode in 'encrypt e decrypt d'.split():
                return mode
            elif mode in 'exit quit'.split():
                break
            else:
                print("Enter either 'encrypt' or 'e' for Encryption or 'decrypt' or 'd' for Dycryption")
    def getMessage():
        print("Enter the message:")
        message = str(input())
        message = message.lower()
        return message

    def generateKey(message):
        key = ''.join([random.choice(string.ascii_letters) for n in range(len(message))])
        key = key.lower()
        return key

    def getKey():
        print("Enter the key:")
        key = str(input())
        key = key.lower()
        return key

    def cipherText(message,key):
        encrypted_message =''
        index = 0
        for symbol in message:
            temp = (alphabet_to_number_dict[symbol] + alphabet_to_number_dict[key[index]]) % 26
            encrypted_message = encrypted_message +number_to_alphabet_dict[temp]
            index = index + 1
            if index == len(key):
                index = 0
        return encrypted_message

    def plainText(message,key):
        decrypted_message =''
        index = 0
        for symbol in message:
            temp = (alphabet_to_number_dict[symbol] - alphabet_to_number_dict[key[index]]) % 26
            decrypted_message = decrypted_message +number_to_alphabet_dict[temp]
            index = index + 1
            if index == len(key):
                index = 0
        return decrypted_message
    
    while True:
        print("Do you want to encrypt or decrypt")
        mode = str(input()).lower()
        if mode in 'encrypt e decrypt d'.split():
            if mode[0]=='e':
                message = getMessage()
                key = generateKey(message)
                print("Plain Message is {0}".format(message))
                print("Encryption Key is {0}".format(key))
                cipher_text = cipherText(message,key)
                print("Encrypted Message is {0}".format(cipher_text))
            elif mode[0]=='d':
                message = getMessage()
                key = getKey()
                print("Cipher Message is {0}".format(message))
                print("Decryption Key is {0}".format(key))
                plain_text = plainText(message,key)
                print("Plain Message is {0}".format(plain_text))
            else:
                print("Enter either 'encrypt' or 'e' for Encryption or 'decrypt' or 'd' for Dycryption.")  
        ch=input("Want to continue(y/n)?: ")
    
