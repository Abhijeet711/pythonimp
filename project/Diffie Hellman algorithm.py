from __future__ import print_function
print("DIFFIE ALGORITHM")
print("-----------------------------------------------")

# Variables Used
sharedPrime = int(input("Enter Shared Prime No.: "))   # p
sharedBase = int(input("Enter Shared Base No.: "))     # g
 
aSecret = int(input("Enter Secret of 1st Person: "))    # a
bSecret = int(input("Enter Secret of 2nd Person: "))      # b
 
# Begin

print( "Publicly Shared Variables are >> ")
print( "Publicly Shared Prime: " , sharedPrime )
print( "Publicly Shared Base:  " , sharedBase )
print("")
# 1st Person Sends 2nd Person A = g^a mod p
A = (sharedBase**aSecret) % sharedPrime
print("1st Person Sends Over Public Chanel: " , A )
 
# 2nd Person Sends 1st Person B = g^b mod p
B = (sharedBase ** bSecret) % sharedPrime
print("2nd Person Sends Over Public Chanel: ", B )
 
print("-----------------------------------------------")
print( "Privately Calculated Shared Secret: " )
# 1st Person Computes Shared Secret: s = B^a mod p
aSharedSecret = (B ** aSecret) % sharedPrime
print( " 1st Person Shared Secret: ", aSharedSecret )
 
# 2nd Person Computes Shared Secret: s = A^b mod p
bSharedSecret = (A**bSecret) % sharedPrime
print( " 2nd Person Shared Secret: ", bSharedSecret )
