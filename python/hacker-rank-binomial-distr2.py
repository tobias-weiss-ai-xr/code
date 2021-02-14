#!/usr/bin/env python3
def fact(x):
    return 1 if x <= 1 else x * fact(x-1)

def comb(n, k):
    return fact(n) / (fact(n-k) * fact(k))

def b(n, k, p):
    return comb(n, k) * p**k * (1-p)**(n-k)


print(round(sum([b(10, k, 0.12) for k in range(3)]), 3))

print(round(sum([b(10, k, 0.12) for k in range(2, 11)]), 3))
