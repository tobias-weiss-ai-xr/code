# coding: utf-8
# Bloom filters for dummies
# https://prakhar.me/articles/bloom-filters-for-dummies/


def h(x):
    return int("".join([v for i, v in enumerate(bin(x)[2:])
                        if i % 2 == 0]), 2) % 11


def g(x):
    return int("".join([v for i, v in enumerate(bin(x)[2:])
                        if i % 2 == 1]), 2) % 11


test = list(map(lambda x: (h(x), g(x)), (25, 159, 585)))
print(test)
