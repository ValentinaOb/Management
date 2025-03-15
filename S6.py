p=1011
a=10


def fermat_little_theorem(a, p):
    # a^(p-1) ≡ 1 (mod p)
    if p > 1 and is_prime(p) and a % p != 0:
        return pow(a, p-1, p) == 1
    return False

def is_prime(n):
    #Simple check if n is a prime number
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


a=fermat_little_theorem(a, p)
print('Fermats theorem: ', a)


# B get
x=4
X=a**x %p
k1=X**y %p

#A get
y=2
Y=a**y %p
k=Y**x %p


print('k: ', k, '  k1: ',k1, '  a**(x*y) %p: ',a**(x*y) %p)
print('k = k1 = a**(xy) %p: ', k==k1==a**(x*y) %p)
