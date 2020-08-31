#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n,m, queries):
    array = [0] * n

    for x in range(m):
        index = queries[x][0]-1
        for a in range(queries[x][1]-(queries[x][0]-1)):
            array[index] += queries[x][2]
            index +=1

    print(max(array))


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n,m,queries)
