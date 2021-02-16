#!/bin/python3

import math

n = 10
x = [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]
y = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]


def mean(x):
    return sum([x_i for x_i in x]) / len(x)


def std(x):
    return (sum([(x_i - mean(x))**2 for x_i in x])/n) ** (1 / 2)


def roh(x, y):
   return sum([((x_i - mean(x)) * (y_i - mean(y))) for x_i, y_i in zip(x, y)]) / (n * std(x) * std(y))


print(mean(x))
print(std(x))
print(mean(y))
print(std(y))
print(round(roh(x, y), 3))
