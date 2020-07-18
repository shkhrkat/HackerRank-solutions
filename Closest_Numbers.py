#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    diff=[]
    for i in range(1, len(arr)):
        diff.append(arr[i]-arr[i-1])
    p= diff.index(min(diff))
    pl=[]
    pl.append(p)
    arr1=[]

    for j in range(len(diff)):
        if j!=p:
            if diff[j]==diff[p]:
                pl.append(j)
    for x in pl:
        arr1.append(arr[x])
        arr1.append(arr[x+1])
    return arr1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
