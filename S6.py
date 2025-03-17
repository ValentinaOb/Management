import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primitive_root(p):
    required_set = {num for num in range(1, p) if pow(num, p - 1, p) == 1}
    for g in range(2, p):
        generated_set = {pow(g, powers, p) for powers in range(1, p)}
        if required_set == generated_set:
            return g
    return None

def gcd(a, b):
    # GCD (Greatest common divisor)
    while b:
        a, b = b, a % b
    return a

def diffie_hellman_key_exchange():
    #Diffie–Hellman (DH) key exchange

    while True:
        p = random.randint(1000, 9999)
        if is_prime(p):
            break
    

    a = find_primitive_root(p)
    if a is None:
        return "None a"
    
    print(f"P: {p}")
    print(f"A: {a}")
    

    x = random.randint(2, 9999)  # secret key for A
    y = random.randint(2, 9999)  # secret key for B
    
    
    X = pow(a, x, p)  # A send B (public keys)
    Y = pow(a, y, p)  # B send A (public keys)
    
    
    k = pow(Y, x, p)  # A calculate common key
    k1 = pow(X, y, p)  # B calculate common key
    
    print('Secret key A, x: ', x)
    print('Secret key B, y: ', y)
    
    print('Public key A, X: ', X)
    print('Public key B, Y: ', Y)

    print('Common key A, k: ', k)
    print('Common key B, k1: ', k1)

    
    if k == k1:
        print("Successfully")
    else:
        print('! Error !')


diffie_hellman_key_exchange()
