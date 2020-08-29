#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c,n):
    jumps = 0
    index = 0

    while index < n-2 :
        oneJump = c[index+1]
        doubleJump = c[index+2]
        if doubleJump==0:
            jumps+=1
            index = index + 2
            continue
        elif oneJump==0:
            jumps+=1
            index = index + 1
            continue

    if index==(n-2):
        jumps+=1

    return jumps



if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c,n)

    print(result)
