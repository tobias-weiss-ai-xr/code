#!/usr/bin/env python3
import math


def norm(x, mu, var):
    return 1 / (math.sqrt(var * 2 * math.pi)) * math.exp(-(x - mu) ** 2 / (2 * var))


mean, std = 70, 10
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# > 80
print('{:.2f}'.format(1 - cdf(80) * 100))
# >= 60
print('{:.2f}'.format(1 - cdf(60) * 100))
# < 60
print('{:.2f}'.format(cdf(60) * 100))
