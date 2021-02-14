#!/usr/bin/env python3
# coding: utf-8
L = []
nmax = 100

for n in range(2, nmax):
    for fact in L:
        if n % fact == 0:
            break
    else:
        L.append(n)
print(L)
