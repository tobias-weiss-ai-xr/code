#!/usr/bin/env python3
import math

max_weight = 9800
n = 49
mu = 205
var = 15**2


def norm(x, mu, var):
    return 1 / (math.sqrt(var * 2 * math.pi)) * math.exp(-(x - mu) ** 2 / (2 * var))


def norm_cdf(x, mu, var):
    return 0.5 * (1 + math.erf((x - mu) / (math.sqrt(2 * var))))


print('{:.4f}'.format(norm_cdf(max_weight / n, mu, var)))
print('{:.4f}'.format(norm_cdf(max_weight, mu*n, var*n)))
