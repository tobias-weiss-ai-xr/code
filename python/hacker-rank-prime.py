#!/usr/bin/env pyhton3
from random import randint

for _ in range(100):
    num = randint(0, 10000)
    if num == 1:
        print("Not prime")
    else:
        if num % 2 == 0 and num > 2:
            print("Not prime")
        else:
            for i in range(3, int(pow(num, 1/2))+1, 2):
                if num % i == 0:
                    print("Not prime")
                    break
            # for-else (finally)
            else:
                print("Prime")


