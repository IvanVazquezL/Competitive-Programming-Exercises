#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n,m, queries):
    #To adjust the indexes with the queries ranges
    array = [0] * (n+2)

    #Make an array with the deltas between each range
    for x in range(m):
        start = queries[x][0]
        value = queries[x][2]
        next = queries[x][1]+1
        array[start] += value

        if next <= n:
            array[next] -= value

        print((array))

    max = 0
    sum = 0
    b = 1
    for a in range(n):
        sum += array[b]

        if max < sum:
            max = sum

        b +=1


    print((array))
    print(max)

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n,m,queries)
