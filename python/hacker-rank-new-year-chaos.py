#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def minimumBribes(Q):
    bribes = 0
    Q = [P-1 for P in Q] # normalize index
    for i, P in enumerate(Q):
        if P -i > 2:
            print("Too chaotic!")
            return
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                bribes += 1
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
