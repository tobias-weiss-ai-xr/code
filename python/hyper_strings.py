#!/bin/python3

import os
import sys
import math

#
# Complete the hyperStrings function below.
#
def hyperStrings(m, H):
    neu = list("init")
    while len(neu) > 0:
        neu = appendItems(H)
        H = H + neu
    print(H)
    return int(len(H)+1 % 1000000007)
   
def appendItems(H):
    neu = list()
    for ele1 in H:
        for ele2 in H:
            ele = str(ele1+ele2)
            if len(ele) <= m and ele not in neu and ele not in H:
                neu.append(ele)
    return neu

if __name__ == '__main__':
    n = int(3)

    m = int(100)

    H = ["a", "ab", "c"]

    result = hyperStrings(m, H)
    print(result)