#!/usr/bin/env python3
import math

n = 100
mu = 500
var = 80 ** 2


def norm(x, mu, var):
    return 1 / (math.sqrt(var * 2 * math.pi)) * math.exp(-(x - mu) ** 2 / (2 * var))


def norm_cdf(x, mu, var):
    return 0.5 * (1 + math.erf((x - mu) / (math.sqrt(2 * var))))


# z-score: 1.96 = (x - mu)/ (var/n)**0.5
A = -1.96 * (var / n) ** 0.5 + mu

B = 1.96 * (var / n) ** 0.5 + mu

print('{:.2f}'.format(A))
print('{:.2f}'.format(B))
