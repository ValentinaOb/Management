p,q,n,E,D=3,11,33,7,3
#n=p*q   
#E must be prime, less than and Not be a factor of the (p-1)*(q-1) 
#D (D*E)/T =1 | (D*E) mod T=1

#Encr M^E mod N = Cipher     |   Cipher^D mod N = M
#Encr with Public Key (E), Decript with Private key(D)
#60^E mod n = X    | X^D mod n =60
T=(p-1)*(q-1)

M=2
DE=1%E
C=2**E%n
X=(C**p)%n

alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
small = alphabet.lower().split(' ')
new_el=[]


def encrypt(m):
    cipher = m**E %n
    return cipher

def decrypt(cipher):
    message = cipher**D %n
    return message
    
def hash_alg():
    k=-1
    sum=0
    for i in range (26):
        k+=1
        sum+=k
    h=sum%n
    return h


f = open("RSA.txt", "r")
M=int(f.read())
f.close()
'''M=60
E=29
D=41
p,q=7,19
n=p*q'''

print('Message: ',M)


cipher=encrypt(M)
print('cipher: ',cipher)

message = decrypt(cipher)
print('message: ',message)

h=hash_alg()
print('Hash: ',h)


#print(60**29 %133)
#print(86**41 %133)

f = open("RSA.txt", "w")
f.write(str(message))
f.close()
