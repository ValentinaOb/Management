p,q,n,E,D=3,11,33,7,3
#n=p*q   
#E must be prime, less than and Not be a factor of the (p-1)*(q-1) 
#D (D*E)/T =1 | (D*E) mod T=1

#Encr M^E mod N = Cipher     |   Cipher^D mod N = M
#Encr with Public Key (E), Decript with Private key(D)
#60^E mod n = X    | X^D mod n =60

T=(p-1)*(q-1)

#DE=1%E
#C=2**E%n
#X=(C**p)%n
cipher=[]
message=[]
h=[]


def encrypt(m):
    if len(m)!=1:
        for i in m:
            cipher.append(i**E %n)
    else: 
        cipher.append(m[0]**E %n)

    return cipher

def decrypt(cipher):
    if len(cipher)!=1:
        for i in cipher:
            message.append(i**D %n)
    else:
        message.append(cipher[0]**D %n)
    return message
    
def hash_alg(m):
    #h=sum(int(digit) for digit in str(i))
    h=sum(m)
    return h

def sign(m):
    P=[]
    if len(m)!=1:
        for i in m:
            P.append(i**E %n)
    else:
        P.append(m[0]**E %n)
    return P

def is_sign(P):
    new=[]
    if len(P)!=1:
        for i in P:
            new.append(i**D %n)
    else:
        new.append(P[0]**D %n)
    
    return new


f = open("RSA.txt", "r")
M= list(map(int, (f.read().split(' '))))

f.close()
'''M=60
E=29
D=41
p,q=7,19
n=p*q'''

print('Message: ',M)

cipher=encrypt(M)
print('cipher: ',cipher)

h=hash_alg(M)
print('Hash: ',h)


P=sign(M)
print('P: ',P)

#print(60**29 %133)
#print(86**41 %133)

f = open("RSA.txt", "w")

data=' '.join(str(x) for x in M)+' : '+' '.join(str(x) for x in P)
f.write(data)
f.close()


# !!!
print('\n')

f = open("RSA.txt", "r")
d=f.read().split(' : ')
M, P=list(map(int,d[0].split(' '))), list(map(int,d[1].split(' ')))
f.close()

#P=[3]

M1=is_sign(P)
print('M: ',M,', M1: ',M1, '  -  ',M==M1)

message = decrypt(cipher)
print('De. Message: ',message)

h1=hash_alg(message)
print('Hash1: ',h1)

print('Hash ? Hash1   -   ',h==h1)

f = open("RSA.txt", "w")
f.write(' '.join(str(x) for x in M))
f.close()