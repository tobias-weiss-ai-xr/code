#!/bin/python3
import math
import os
import random
import re
import sys

OUTPUT_PATH = "./hacker-rank-hourglass.txt"

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = 0
    for i in range(0, len(arr)-2):
        for j in range(0, len(arr[i])-2):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                    arr[i+1][j+1] + \
                    arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum > max_sum:
                max_sum = sum
    return max_sum


if __name__ == '__main__':
    fptr = open(OUTPUT_PATH, 'r')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, fptr.readline().rstrip().split())))

    result = hourglassSum(arr)
    print("result:", result)

    fptr.close()
