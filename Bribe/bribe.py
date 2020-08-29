#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q,n):
    rest = []
    for x in range(n-1):
        rest.append(q[x]-q[x+1])

    print(rest)
    positive = [b for b in rest if b >= 0 ]

    print(positive)

    for c in positive:
        if c > 2:
            return "Too chaotic"

    return sum(positive)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q,n))

    
