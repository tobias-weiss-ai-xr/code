#!/usr/bin/env python3
def factorial(x):
    if x > 1:
        return x * factorial(x - 1)
    else:
        return 1


def binomial_coefficient(n, k):
    return (factorial(n)) / (factorial(n - k) * factorial(k))


def binomial_distribution(n, k, p):
    return binomial_coefficient(n, k) * p**k * (1-p)**(n - k)


arr = [1.09, 1.0]

p_male = arr[0] / (arr[0] + arr[1])

# binomail probability for more than 3 boys out of 6
p = 0.0
for i in range(3, 7):
    p += binomial_distribution(6, i, p_male)

print('{:.3f}'.format(p))


def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


def comb(n, x):
    return fact(n) / (fact(x) * fact(n - x))


def b(x, n, p):
    return comb(n, x) * p ** x * (1 - p) ** (n - x)


l, r = [1.09, 1.0]
odds = l / r
print(round(sum([b(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))
