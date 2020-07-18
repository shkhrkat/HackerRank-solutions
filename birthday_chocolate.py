import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    if m<len(s):
        k=0
        for i in range(len(s)-m):
            sum=s[i]
            for j in range(1,m):
                sum=sum+s[i+j]
            if sum==d:
                k=k+1
        return k
    else:
        if d==s[0]:
            return 1
        else:
            return 0
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
