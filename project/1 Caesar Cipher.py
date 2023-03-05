print("Caesar Cipher (Encryption and Decryption)")
ch='y'
while ch.lower()=='y':
    plaintext = input(" Enter your plaintext: ")
    shift = input(" enter your key: ")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""

    # shift value can only be an integer
    while isinstance(int(shift), int) == False:
      # asking the user to re-enter the shift value
      
      shift = input("Please enter your key integers only: ")

    shift = int(shift)
      
    new_ind = 0 # this value will be changed later
    for i in plaintext:
      if i.lower() in alphabet:
        new_ind = alphabet.index(i) + shift
        ciphertext += alphabet[new_ind % 26]
      else:
        ciphertext += i    
    print("The ciphertext is: " + ciphertext)
    ch=input("Want to continue(y/n)?: ")

