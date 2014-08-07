from random import randint

def test_prime(p):
    '''False positives on Carmichael numbers (which are rare).
    If p is composite but not a Carmichael number, returns False with probability at least 1/2'''
    a = randint(1,p-1)
    return pow(a,p-1,p) == 1

def is_prime(p, n = 20):
    "If p is composite but not a Carmichael number, returns False with probability at least 1-(1/2)^n"
    for i in range(n):
        if not test_prime(p): return False
    return True

def find_prime(a,b):
    "returns a 'prime' between a and b"
    while True:
        p = randint(a,b)
        if is_prime(p): return p

"""
p = find_prime(1e10, 2e10)
q = find_prime(1e10, 2e10)
N = p*q
"""
