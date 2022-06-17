import math
message = int(input("Enter the message to be decrypt: "))

p = 3
q = 11
e = 3
 
n = p*q
i = (p-1)*(q-1)
d = pow(e, -1, i)

def decrypt(me):
    m = pow(me,d,n)
    print("Decrypted Message is: ", c)
    return c

print("Encrypted message is: ", message)
c = decrypt(message)
