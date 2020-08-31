#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q,n):
    bribe = 0
    c = len(q)-1
    for a in range(len(q)):


        if (q[c] - (c + 1)) > 2:
            return "Too chaotic"

        b = max(0,q[c]-2)
        while b<c:
            print(q[b],">",q[c])
            if q[b] > q[c]:
                bribe += 1

            b +=1
        c += -1

    return bribe

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q,n))
