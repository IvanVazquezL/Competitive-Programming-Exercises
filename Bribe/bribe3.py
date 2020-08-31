#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q,n):
    bribe = 0
    q = [x-1 for x in q]

    for i,x in enumerate(q):

        #If any element of the array is ahead 2 places
        if x - i > 2:
            return "Too chaotic"

        #Who bribed x
        for j in range(max(x-1,0),i):
            if q[j] > x:
                bribe += 1

    return bribe

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q,n))
